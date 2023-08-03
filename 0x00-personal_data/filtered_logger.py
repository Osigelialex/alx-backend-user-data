#!/usr/bin/env python3
"""Filtered logger module"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    pattern = fr'({re.escape(separator)}|^)({"|".join(re.escape(field) for field in fields)})=(.*?)(?={re.escape(separator)}|$)'
    return re.sub(pattern, rf'\1\2={redaction}', message)