#!/usr/bin/env python3
"""
Authorization module for the API
"""
from flask import request
from typing import List, TypeVar
from os import getenv

SESSION_NAME = getenv('SESSION_NAME')


class Auth:
    """
    Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for the given path.
        Args:
            path (str): The path to check.
            excluded_paths (List[str]):excluded from authentication.
        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        # WE ADD SLASH TO ALL CASES FOR CONSISTENCY
        # Add wildcard if missing
        if path[-1] is not '/':
            path += '/'

        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.
        Args:
            request: The Flask request object.
        Returns:
            str: The value of the authorization header.
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get current user from request
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request
        """
        if request is None:
            return None

        session_cookie = request.cookies.get(SESSION_NAME)
        return session_cookie
