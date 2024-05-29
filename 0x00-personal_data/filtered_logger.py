#!/usr/bin/env python3
"""script for task 0"""
import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """ perform the substitution with a single regex."""
    for field in fields:
        pattern = f"{field}=[^{separator}]+"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message
