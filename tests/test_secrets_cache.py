from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from infisical_sdk.api_types import BaseSecret
from infisical_sdk.resources.secrets import V3RawSecrets
from infisical_sdk.util import SecretsCache


def make_secret(value):
    return BaseSecret.from_dict({
        "id": "id",
        "_id": "id",
        "workspace": "project",
        "environment": "dev",
        "version": 1,
        "type": "shared",
        "secretKey": "API_KEY",
        "secretValue": value,
        "secretComment": "",
        "createdAt": "2026-01-01T00:00:00Z",
        "updatedAt": "2026-01-01T00:00:00Z",
    })


@pytest.fixture
def cache():
    cache = SecretsCache(ttl_seconds=60)
    yield cache
    cache.close()


def make_client(cache, values):
    requests = MagicMock()
    requests.get.side_effect = [
        SimpleNamespace(data=SimpleNamespace(secret=make_secret(value))) for value in values
    ]
    return V3RawSecrets(requests, cache), requests


@pytest.mark.parametrize(
    ("first", "second"),
    [
        ({"project_slug": "project-a"}, {"project_slug": "project-b"}),
        ({"project_id": "p1", "version": "1"}, {"project_id": "p1"}),
        ({"project_id": "p1", "view_secret_value": False}, {"project_id": "p1"}),
        ({"project_id": "p1", "expand_secret_references": False}, {"project_id": "p1"}),
        ({"project_id": "p1", "include_imports": False}, {"project_id": "p1"}),
    ],
)
def test_get_secret_by_name_does_not_share_cache_across_requests(cache, first, second):
    secrets, requests = make_client(cache, ["first", "second"])
    common = {"secret_name": "API_KEY", "environment_slug": "dev", "secret_path": "/"}

    assert secrets.get_secret_by_name(**common, **first).secretValue == "first"
    assert secrets.get_secret_by_name(**common, **second).secretValue == "second"
    assert requests.get.call_count == 2


def test_get_secret_by_name_uses_cache_for_same_request(cache):
    secrets, requests = make_client(cache, ["first"])
    args = {
        "secret_name": "API_KEY",
        "environment_slug": "dev",
        "secret_path": "/",
        "project_slug": "a",
    }

    assert secrets.get_secret_by_name(**args).secretValue == "first"
    assert secrets.get_secret_by_name(**args).secretValue == "first"
    assert requests.get.call_count == 1


@pytest.mark.parametrize("mutation", ["update_secret_by_name", "delete_secret_by_name"])
def test_mutation_by_slug_invalidates_secret_cached_by_id(cache, mutation):
    secrets, requests = make_client(cache, ["old", "new"])
    requests.patch.return_value = SimpleNamespace(data=SimpleNamespace(secret=make_secret("new")))
    requests.delete.return_value = SimpleNamespace(data=SimpleNamespace(secret=make_secret("old")))
    location = {"environment_slug": "dev", "secret_path": "/"}

    assert secrets.get_secret_by_name("API_KEY", project_id="p1", **location).secretValue == "old"
    name_arg = "current_secret_name" if mutation == "update_secret_by_name" else "secret_name"
    getattr(secrets, mutation)(**{name_arg: "API_KEY"}, project_slug="project-a", **location)

    assert secrets.get_secret_by_name("API_KEY", project_id="p1", **location).secretValue == "new"
    assert requests.get.call_count == 2
