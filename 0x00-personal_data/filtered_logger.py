#!/usr/bin/env python3
"""Filtered logger module"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        log_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            log_message, self.SEPARATOR)
        

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates sensitive information in log messages"""
    return re.sub(r'(\b{}=)[^{}]*'.format('|'.join(fields),
                                          separator), r'\1' +
                  redaction, message)
