#!/usr/bin/env python3
"""password hashing module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns hashed form of password"""
    salt = bcrypt.gensalt()
    hashed_password =  bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
