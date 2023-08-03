#!/usr/bin/env python3
"""password hashing module"""
import bcrypt
from typing import Union


def hash_password(password: str) -> Union[bytes, None]:
    """returns hashed form of password"""
    salt = bcrypt.gensalt()
    hashed_password =  bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
