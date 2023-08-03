#!/usr/bin/env python3
"""password hashing module"""
import bcrypt
from typing import Union


def hash_password(password: str) -> Union[bytes, str]:
    """returns hashed form of password"""
    if password == '' or password is None:
        return ''
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
