#!/usr/bin/env python3
"""Filtered logger module"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates sensitive information in log messages
    by replacing specific fields with a redaction string.

    Args:
        fields (List[str]): A list of strings 
        representing the fields to be obfuscated.
        redaction (str): A string representing the 
        replacement for the obfuscated fields.
        message (str): A string representing 
        the log message to be obfuscated.
        separator (str): A string representing the separator 
        used in the log message to distinguish between fields.

    Returns:
        str: The obfuscated log message.
    """
    return re.sub(r'(\b{}=)[^{}]*'.format('|'.join(fields),
                                          separator), r'\1' +
                  redaction, message)
