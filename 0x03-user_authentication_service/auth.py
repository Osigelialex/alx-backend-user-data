#!/usr/bin/env python3
"""module for handling user authentication
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user
        """
        if email is None or password is None:
            return None

        try:
            old_user = self._db.find_user_by(email=email)
            if old_user is not None:
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            pass

        hashed_password = _hash_password(password)
        new_user = self._db.add_user(email, hashed_password)
        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """validates the users credentials
        """
        if email is None or password is None:
            return False

        try:
            user = self._db.find_user_by(email=email)
            password = password.encode('utf-8')

            if user is not None and \
                    bcrypt.checkpw(password, user.hashed_password):
                return True
        except NoResultFound:
            return False

        return False

    def create_session(self, email: str) -> str:
        """Creates a session for the user
        """
        user = None
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        user.session_id = session_id
        return session_id

    def get_user_from_session_id(session_id: str) -> str:
        """Retrieves a user by session id
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None


def _hash_password(password: str) -> bytes:
    """Returns the hashed form of a password
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """Generates a uuid
    """
    return str(uuid.uuid4())
