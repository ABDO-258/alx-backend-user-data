#!/usr/bin/env python3
"""script to encrypt a password"""

import bcrypt


def hash_password(password: str) -> bytes:
    """hash a password """

    # Generate a salt
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """check if password valid"""
    return bcrypt.checkpw(password.encode(), hashed_password)
