#!/usr/bin/env python3
"""password hashing module"""
from bcrypt import hashpw, gensalt


def hash_password(password: str) -> bytes:
    """returns hashed form of password"""
    return hashpw(password.encode(), gensalt())