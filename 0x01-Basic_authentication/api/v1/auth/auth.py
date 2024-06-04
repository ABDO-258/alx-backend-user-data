#!/usr/bin/env python3
"""
module to manage the API authentication.
"""
from typing import List, TypeVar
from flask import request
import fnmatch


class Auth:
    """ class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ doc doc doc string """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != "/":
            path += "/"
        for pattern in excluded_paths:
            if pattern[-1] != "/":
                pattern += "/"
            if fnmatch.fnmatch(path, pattern):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ doc doc doc string """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ doc doc doc string """
        return None
