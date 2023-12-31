#!/usr/bin/env python3
"""Session authentication module
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Class for handling session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns User instance based on cookie value
        """
        cookie = self.session_cookie(request)
        user_id = self.user_id_by_session_id.get(cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """destroys the user session
        """
        if request is None:
            return False

        cookie = self.session_cookie(request)
        if cookie is None:
            return False

        if self.user_id_for_session_id(cookie) is None:
            return False

        del SessionAuth.user_id_by_session_id[cookie]
        return True
