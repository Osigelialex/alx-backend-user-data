#!/usr/bin/env python3
"""password hashing module"""
import bcrypt
from typing import Union


def hash_password(password: str) -> bytes:
    """returns hashed form of password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
