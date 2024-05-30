#!/usr/bin/env python3
"""script for task 0"""
import re
from typing import List
import logging


# Define the PII_FIELDS constant
PII_FIELDS = ("name", "email", "password", "ssn", "date_of_birth")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """doc doc docstring"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """doc doc docstring"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """ perform the substitution with a single regex."""
    for field in fields:
        pattern = f"{field}=[^{separator}]+"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message


def get_logger() -> logging.Logger:
    """Create and return a logger named 'user_data'."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create the StreamHandler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # set the RedactingFormatter as the formatter for the StreamHandler
    formatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    # Add the StreamHandler to the logger
    logger.addHandler(stream_handler)

    return logger
