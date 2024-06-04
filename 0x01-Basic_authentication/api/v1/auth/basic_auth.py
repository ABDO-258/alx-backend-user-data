#!/usr/bin/env python3
"""
module to manage the API authentication.
"""
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """ class to manage the API authentication """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Basic - Base64 part"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        base64 = authorization_header.split(' ', 1)[1]
        return base64

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode with base64"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encoding = base64_authorization_header.encode('utf-8')
            decode_by_64 = b64decode(encoding)
            decoding = decode_by_64.decode('utf-8')
        except BaseException:
            return None
        return decoding

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """return the user credentials"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        email_pass = decoded_base64_authorization_header.split(":", 1)
        return email_pass[0], email_pass[1]
