from typing import Any, Dict, Generic, Optional, TypeVar, Type
import requests
from dataclasses import dataclass

T = TypeVar("T")

def join_url(base: str, path: str) -> str:
    """
    Join base URL and path properly, handling slashes appropriately.
    """
    if not base.endswith('/'):
        base += '/'
    return base + path.lstrip('/')

class InfisicalError(Exception):
    """Base exception for Infisical client errors"""
    pass


class APIError(InfisicalError):
    """API-specific errors"""
    def __init__(self, message: str, status_code: int, response: Dict[str, Any]):
        self.status_code = status_code
        self.response = response
        super().__init__(f"{message} (Status: {status_code})")


@dataclass
class APIResponse(Generic[T]):
    """Generic API response wrapper"""
    data: T
    status_code: int
    headers: Dict[str, str]

    def to_dict(self) -> Dict:
        """Convert to dictionary with camelCase keys"""
        return {
            'data': self.data.to_dict() if hasattr(self.data, 'to_dict') else self.data,
            'statusCode': self.status_code,
            'headers': self.headers
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'APIResponse[T]':
        """Create from dictionary with camelCase keys"""
        return cls(
            data=data['data'],
            status_code=data['statusCode'],
            headers=data['headers']
        )


class InfisicalRequests:
    def __init__(self, host: str, token: Optional[str] = None, verifySSL: bool = True):
        self.host = host.rstrip("/")
        self.session = requests.Session()
        self.verifySSL = verifySSL

        # Set common headers
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

        if token:
            self.set_token(token)

    def _build_url(self, path: str) -> str:
        """Construct full URL from path"""
        return join_url(self.host, path.lstrip("/"))

    def set_token(self, token: str):
        """Set authorization token"""
        self.session.headers["Authorization"] = f"Bearer {token}"

    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response and raise appropriate errors"""
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            try:
                error_data = response.json()
            except ValueError:
                error_data = {"message": response.text}

            raise APIError(
                message=error_data.get("message", "Unknown error"),
                status_code=response.status_code,
                response=error_data
            )
        except requests.exceptions.RequestException as e:
            raise InfisicalError(f"Request failed: {str(e)}")
        except ValueError:
            raise InfisicalError("Invalid JSON response")

    def get(
            self,
            path: str,
            model: Type[T],
            params: Optional[Dict[str, Any]] = None
          ) -> APIResponse[T]:

        """
        Make a GET request and parse response into given model

        Args:
            path: API endpoint path
            model: model class to parse response into
            params: Optional query parameters
        """
        response = self.session.get(self._build_url(path), params=params, verify=self.verifySSL)
        data = self._handle_response(response)

        parsed_data = model.from_dict(data) if hasattr(model, 'from_dict') else data

        return APIResponse(
            data=parsed_data,
            status_code=response.status_code,
            headers=dict(response.headers)
        )

    def post(
            self,
            path: str,
            model: Type[T],
            json: Optional[Dict[str, Any]] = None
          ) -> APIResponse[T]:

        """Make a POST request with JSON data"""

        if json is not None:
            # Filter out None values
            json = {k: v for k, v in json.items() if v is not None}

        response = self.session.post(self._build_url(path), json=json, verify=self.verifySSL)
        data = self._handle_response(response)

        parsed_data = model.from_dict(data) if hasattr(model, 'from_dict') else data

        return APIResponse(
            data=parsed_data,
            status_code=response.status_code,
            headers=dict(response.headers)
        )

    def patch(
            self,
            path: str,
            model: Type[T],
            json: Optional[Dict[str, Any]] = None
          ) -> APIResponse[T]:

        """Make a PATCH request with JSON data"""

        if json is not None:
            # Filter out None values
            json = {k: v for k, v in json.items() if v is not None}

        response = self.session.patch(self._build_url(path), json=json, verify=self.verifySSL)
        data = self._handle_response(response)

        parsed_data = model.from_dict(data) if hasattr(model, 'from_dict') else data

        return APIResponse(
            data=parsed_data,
            status_code=response.status_code,
            headers=dict(response.headers)
        )

    def delete(
            self,
            path: str,
            model: Type[T],
            json: Optional[Dict[str, Any]] = None
          ) -> APIResponse[T]:

        """Make a PATCH request with JSON data"""

        if json is not None:
            # Filter out None values
            json = {k: v for k, v in json.items() if v is not None}

        response = self.session.delete(self._build_url(path), json=json, verify=self.verifySSL)
        data = self._handle_response(response)

        parsed_data = model.from_dict(data) if hasattr(model, 'from_dict') else data

        return APIResponse(
            data=parsed_data,
            status_code=response.status_code,
            headers=dict(response.headers)
        )
