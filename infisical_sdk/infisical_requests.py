from typing import Any, Dict, Generic, Optional, TypeVar, Type, Callable, List
import socket
import requests
import functools
from dataclasses import dataclass
import time
import random

T = TypeVar("T")

# List of network-related exceptions that should trigger retries
NETWORK_ERRORS = [
    requests.exceptions.ConnectionError,
    requests.exceptions.ChunkedEncodingError,
    requests.exceptions.ReadTimeout,
    requests.exceptions.ConnectTimeout,
    socket.gaierror,
    socket.timeout,
    ConnectionResetError,
    ConnectionRefusedError,
    ConnectionError,
    ConnectionAbortedError,
]

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

def with_retry(
    max_retries: int = 3, 
    base_delay: float = 1.0, 
    network_errors: Optional[List[Type[Exception]]] = None
) -> Callable:
    """
    Decorator to add retry logic with exponential backoff to requests methods.
    """
    if network_errors is None:
        network_errors = NETWORK_ERRORS
        
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retry_count = 0
            
            while True:
                try:
                    return func(*args, **kwargs)
                except tuple(network_errors) as error:
                    retry_count += 1
                    if retry_count > max_retries:
                        raise
                    
                    base_delay_with_backoff = base_delay * (2 ** (retry_count - 1))
                    
                    # +/-20% jitter
                    jitter = random.uniform(-0.2, 0.2) * base_delay_with_backoff
                    delay = base_delay_with_backoff + jitter
                    
                    time.sleep(delay)
        
        return wrapper
    
    return decorator


class InfisicalRequests:
    def __init__(self, host: str, token: Optional[str] = None, timeout: Optional[float] = 30):
        self.host = host.rstrip("/")
        self.session = requests.Session()
        self.timeout = timeout

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

    @with_retry(max_retries=4, base_delay=1.0)
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
        response = self.session.get(self._build_url(path), params=params, timeout=self.timeout)
        data = self._handle_response(response)

        parsed_data = model.from_dict(data) if hasattr(model, 'from_dict') else data

        return APIResponse(
            data=parsed_data,
            status_code=response.status_code,
            headers=dict(response.headers)
        )

    @with_retry(max_retries=4, base_delay=1.0)
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

        response = self.session.post(self._build_url(path), json=json, timeout=self.timeout)
        data = self._handle_response(response)

        parsed_data = model.from_dict(data) if hasattr(model, 'from_dict') else data

        return APIResponse(
            data=parsed_data,
            status_code=response.status_code,
            headers=dict(response.headers)
        )

    @with_retry(max_retries=4, base_delay=1.0)
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

        response = self.session.patch(self._build_url(path), json=json, timeout=self.timeout)
        data = self._handle_response(response)

        parsed_data = model.from_dict(data) if hasattr(model, 'from_dict') else data

        return APIResponse(
            data=parsed_data,
            status_code=response.status_code,
            headers=dict(response.headers)
        )

    @with_retry(max_retries=4, base_delay=1.0)
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

        response = self.session.delete(self._build_url(path), json=json, timeout=self.timeout)
        data = self._handle_response(response)

        parsed_data = model.from_dict(data) if hasattr(model, 'from_dict') else data

        return APIResponse(
            data=parsed_data,
            status_code=response.status_code,
            headers=dict(response.headers)
        )
