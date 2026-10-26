<h1 align="center">
  <img width="300" src="/img/logoname-white.svg#gh-dark-mode-only" alt="infisical">
</h1>
<p align="center">
  <p align="center"><b>Infisical Python SDK</b></p>
<h4 align="center">
|
  <a href="https://infisical.com/docs/sdks/languages/python">Documentation</a> |
  <a href="https://www.infisical.com">Website</a> |
  <a href="https://infisical.com/slack">Slack</a> |
</h4>

<h4 align="center">
  <a href="https://github.com/Infisical/python-sdk-official/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="Infisical SDK's are released under the MIT license." />
  </a>
  <a href="https://infisical.com/slack">
    <img src="https://img.shields.io/badge/chat-on%20Slack-blueviolet" alt="Slack community channel" />
  </a>
  <a href="https://twitter.com/infisical">
    <img src="https://img.shields.io/twitter/follow/infisical?label=Follow" alt="Infisical Twitter" />
  </a>
</h4>

## Introduction

**[Infisical](https://infisical.com)** is the open source secret management platform that teams use to centralize their secrets like API keys, database credentials, and configurations.

If you’re working with Python, the official Infisical Python SDK package is the easiest way to fetch and work with secrets for your application. You can read the documentation [here](https://infisical.com/docs/sdks/languages/python).

## Documentation
You can find the documentation for the Python SDK on our [SDK documentation page](https://infisical.com/docs/sdks/languages/python).

## Self-hosted instances with a private CA

The SDK uses `requests`, which verifies TLS certificates against the Mozilla CA bundle from the `certifi` package. It does not read your operating system trust store.

If your self-hosted Infisical instance uses a certificate from a private or corporate CA, set `REQUESTS_CA_BUNDLE` to a CA bundle file that contains that CA:

```bash
# Debian / Ubuntu
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

# Fedora / RHEL
export REQUESTS_CA_BUNDLE=/etc/pki/tls/certs/ca-bundle.crt
```

These paths are the operating system bundles, so the CA must be added there first (for example with `update-ca-certificates` or `update-ca-trust`). You can also point `REQUESTS_CA_BUNDLE` to a PEM file that holds only your CA.

## JWT authentication

For a Machine Identity configured with JWT Auth, use `jwt_auth` (OIDC Auth is a separate method):

```python
from infisical_sdk import InfisicalSDKClient

with InfisicalSDKClient(host="https://us.infisical.com") as client:
    auth = client.auth.jwt_auth.login(identity_id=identity_id, jwt=identity_jwt)
    # Subsequent SDK requests use the returned access token automatically.
```

Pass `organization_slug="your-org"` to scope the login to an organization.
See the [JWT Auth API reference](https://infisical.com/docs/api-reference/endpoints/jwt-auth/login).

Run the offline regression tests with `pytest tests` after installing `test-requirements.txt`.

## Security

Please do not file GitHub issues or post on our public forum for security vulnerabilities, as they are public!

Infisical takes security issues very seriously. If you have any concerns about Infisical or believe you have uncovered a vulnerability, please get in touch via the e-mail address security@infisical.com. In the message, try to provide a description of the issue and ideally a way of reproducing it. The security team will get back to you as soon as possible.

Note that this security address should be used only for undisclosed vulnerabilities. Please report any security problems to us before disclosing it publicly.