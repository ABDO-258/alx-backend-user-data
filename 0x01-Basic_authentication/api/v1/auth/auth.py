#!/usr/bin/env python3
"""
module to manage the API authentication.
"""
from typing import List, TypeVar
from flask import request



class Auth:
    """ class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ doc doc doc string """
        return False
    

    def authorization_header(self, request=None) -> str:
        """ doc doc doc string """
        if request is None:
            return None
        return request.headers.get("Authorization", None)


    def current_user(self, request=None) -> TypeVar('User'):
        """ doc doc doc string """
        return None