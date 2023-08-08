#!/usr/bin/env python3
"""API authentication management module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Manages the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """applies required auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user function
        """
        return None
