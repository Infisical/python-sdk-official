import os
import json
import base64
import requests
from typing import Dict
from datetime import datetime
import hashlib
import hmac
import urllib.parse


class AWSAuth:
    def __init__(self, client):
        self.client = client

    def aws_iam_auth_login(self, identity_id: str = "") -> Dict:
        if not identity_id:
            identity_id = os.getenv("INFISICAL_AWS_IAM_AUTH_IDENTITY_ID")

        aws_region = self._get_aws_region()
        credentials = self._get_aws_credentials()

        # Prepare request for signing
        iam_request_url = f"https://sts.{aws_region}.amazonaws.com/"
        iam_request_body = "Action=GetCallerIdentity&Version=2011-06-15"

        # Create request
        req = {
            "method": "POST",
            "url": iam_request_url,
            "data": iam_request_body,
            "headers": {}
        }

        # Add date header
        current_time = datetime.utcnow()
        req["headers"]["X-Amz-Date"] = current_time.strftime("%Y%m%dT%H%M%SZ")

        # Calculate payload hash
        payload_hash = hashlib.sha256(iam_request_body.encode()).hexdigest()

        # Sign the request
        self._sign_request(req, credentials, payload_hash, "sts", aws_region, current_time)

        # Prepare headers for the API call
        real_headers = {k: v for k, v in req["headers"].items() if k.lower() != "content-length"}
        real_headers["Host"] = f"sts.{aws_region}.amazonaws.com"
        real_headers["Content-Type"] = "application/x-www-form-urlencoded; charset=utf-8"
        real_headers["Content-Length"] = str(len(iam_request_body))

        # Convert headers to JSON and encode
        json_string_headers = json.dumps(real_headers)
        encoded_headers = base64.b64encode(json_string_headers.encode()).decode()

        # Prepare the request body for the API call
        api_request = {
            "HTTPRequestMethod": req["method"],
            "IamRequestBody": base64.b64encode(iam_request_body.encode()).decode(),
            "IamRequestHeaders": encoded_headers,
            "IdentityId": identity_id
        }

        # Call the API
        credential = self._call_aws_iam_auth_login(api_request)

        # Set the access token
        self.client.set_access_token(credential["accessToken"], "AWS_IAM")


        return credential

    def _get_aws_region(self):
        # Implement AWS region retrieval logic here
        # For this example, we'll use a placeholder
        return "us-west-2"

    def _get_aws_credentials(self):
        # Implement AWS credentials retrieval logic here
        # For this example, we'll use placeholders
        return {
            "AccessKeyId": "YOUR_ACCESS_KEY_ID",
            "SecretAccessKey": "YOUR_SECRET_ACCESS_KEY",
            "SessionToken": "YOUR_SESSION_TOKEN"
        }

    def _sign_request(self, req, credentials, payload_hash, service, region, time):
        # Implement AWS Signature V4 signing process
        # This is a simplified version and may need to be expanded for full functionality
        algorithm = "AWS4-HMAC-SHA256"
        credential_scope = f"{time.strftime('%Y%m%d')}/{region}/{service}/aws4_request"

        string_to_sign = f"{algorithm}\n{req['headers']['X-Amz-Date']}\n{credential_scope}\n"
        string_to_sign += hashlib.sha256(self._canonical_request(req, payload_hash).encode()).hexdigest()

        date_key = hmac.new(f"AWS4{credentials['SecretAccessKey']}".encode(), time.strftime('%Y%m%d').encode(),
                            hashlib.sha256).digest()
        date_region_key = hmac.new(date_key, region.encode(), hashlib.sha256).digest()
        date_region_service_key = hmac.new(date_region_key, service.encode(), hashlib.sha256).digest()
        signing_key = hmac.new(date_region_service_key, b"aws4_request", hashlib.sha256).digest()

        signature = hmac.new(signing_key, string_to_sign.encode(), hashlib.sha256).hexdigest()

        req["headers"]["Authorization"] = (
            f"{algorithm} Credential={credentials['AccessKeyId']}/{credential_scope}, "
            f"SignedHeaders=host;x-amz-date, Signature={signature}"
        )

    def _canonical_request(self, req, payload_hash):
        canonical_headers = "host:" + req["headers"]["Host"] + "\n" + "x-amz-date:" + req["headers"][
            "X-Amz-Date"] + "\n"
        signed_headers = "host;x-amz-date"

        return f"{req['method']}\n/{urllib.parse.urlparse(req['url']).path}\n\n{canonical_headers}\n{signed_headers}\n{payload_hash}"

    def _call_aws_iam_auth_login(self, request):
        response = requests.post(
            f"{self.client.base_url}/v1/auth/aws-auth/login",
            json=request
        )
        response.raise_for_status()
        return response.json()