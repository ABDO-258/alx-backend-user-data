#!/usr/bin/env python3
"""
module to manage the API authentication.
"""
from api.v1.auth.auth import Auth


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
