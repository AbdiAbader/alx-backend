#!/usr/bin/env python3
"""Simple helper"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """a tuple of size two containing a start index
    and an end index corresponding to
    the range of indexes"""
    end = page_size * page
    return (end-page_size, end)
