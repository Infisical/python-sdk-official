# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from infisicalapi_client.models.api_v1_dynamic_secrets_post_request_provider_any_of import ApiV1DynamicSecretsPostRequestProviderAnyOf
from infisicalapi_client.models.api_v1_dynamic_secrets_post_request_provider_any_of1 import ApiV1DynamicSecretsPostRequestProviderAnyOf1
from infisicalapi_client.models.api_v1_dynamic_secrets_post_request_provider_any_of2 import ApiV1DynamicSecretsPostRequestProviderAnyOf2
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

APIV1DYNAMICSECRETSPOSTREQUESTPROVIDER_ANY_OF_SCHEMAS = ["ApiV1DynamicSecretsPostRequestProviderAnyOf", "ApiV1DynamicSecretsPostRequestProviderAnyOf1", "ApiV1DynamicSecretsPostRequestProviderAnyOf2"]

class ApiV1DynamicSecretsPostRequestProvider(BaseModel):
    """
    The type of dynamic secret.
    """

    # data type: ApiV1DynamicSecretsPostRequestProviderAnyOf
    anyof_schema_1_validator: Optional[ApiV1DynamicSecretsPostRequestProviderAnyOf] = None
    # data type: ApiV1DynamicSecretsPostRequestProviderAnyOf1
    anyof_schema_2_validator: Optional[ApiV1DynamicSecretsPostRequestProviderAnyOf1] = None
    # data type: ApiV1DynamicSecretsPostRequestProviderAnyOf2
    anyof_schema_3_validator: Optional[ApiV1DynamicSecretsPostRequestProviderAnyOf2] = None
    if TYPE_CHECKING:
        actual_instance: Union[ApiV1DynamicSecretsPostRequestProviderAnyOf, ApiV1DynamicSecretsPostRequestProviderAnyOf1, ApiV1DynamicSecretsPostRequestProviderAnyOf2]
    else:
        actual_instance: Any
    any_of_schemas: List[str] = Field(APIV1DYNAMICSECRETSPOSTREQUESTPROVIDER_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = ApiV1DynamicSecretsPostRequestProvider.construct()
        error_messages = []
        # validate data type: ApiV1DynamicSecretsPostRequestProviderAnyOf
        if not isinstance(v, ApiV1DynamicSecretsPostRequestProviderAnyOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiV1DynamicSecretsPostRequestProviderAnyOf`")
        else:
            return v

        # validate data type: ApiV1DynamicSecretsPostRequestProviderAnyOf1
        if not isinstance(v, ApiV1DynamicSecretsPostRequestProviderAnyOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiV1DynamicSecretsPostRequestProviderAnyOf1`")
        else:
            return v

        # validate data type: ApiV1DynamicSecretsPostRequestProviderAnyOf2
        if not isinstance(v, ApiV1DynamicSecretsPostRequestProviderAnyOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiV1DynamicSecretsPostRequestProviderAnyOf2`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in ApiV1DynamicSecretsPostRequestProvider with anyOf schemas: ApiV1DynamicSecretsPostRequestProviderAnyOf, ApiV1DynamicSecretsPostRequestProviderAnyOf1, ApiV1DynamicSecretsPostRequestProviderAnyOf2. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1DynamicSecretsPostRequestProvider:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1DynamicSecretsPostRequestProvider:
        """Returns the object represented by the json string"""
        instance = ApiV1DynamicSecretsPostRequestProvider.construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[ApiV1DynamicSecretsPostRequestProviderAnyOf] = None
        try:
            instance.actual_instance = ApiV1DynamicSecretsPostRequestProviderAnyOf.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[ApiV1DynamicSecretsPostRequestProviderAnyOf1] = None
        try:
            instance.actual_instance = ApiV1DynamicSecretsPostRequestProviderAnyOf1.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[ApiV1DynamicSecretsPostRequestProviderAnyOf2] = None
        try:
            instance.actual_instance = ApiV1DynamicSecretsPostRequestProviderAnyOf2.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ApiV1DynamicSecretsPostRequestProvider with anyOf schemas: ApiV1DynamicSecretsPostRequestProviderAnyOf, ApiV1DynamicSecretsPostRequestProviderAnyOf1, ApiV1DynamicSecretsPostRequestProviderAnyOf2. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


