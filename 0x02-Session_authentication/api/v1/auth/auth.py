#!/usr/bin/env python3
"""API authentication management module
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Manages the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """defines routes that don't need authentication
        """
        if not path or not excluded_paths or len(excluded_paths) == 0:
            return True

        if any([path in x for x in excluded_paths]):
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization header
        """
        if request and request.headers.get('Authorization'):
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user function
        """
        return None

    def session_cookie(self, request=None):
        """returns cookie value from request
        """
        if request is None:
            return None

        cookie_name = os.getenv('SESSION_NAME', None)
        return request.cookies.get(cookie_name)
