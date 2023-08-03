#!/usr/bin/env python3
"""password hashing module"""
import bcrypt
from typing import Union


def hash_password(password: str) -> Union[bytes, None]:
    """returns hashed form of password"""
    if password is None or not isinstance(password, str):
        return None
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
