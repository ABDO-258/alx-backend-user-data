#!/usr/bin/env python3
"""script to encrypt a password"""

import bcrypt


def hash_password(password: str) -> bytes:
    """hash a password """

    # Generate a salt
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password
