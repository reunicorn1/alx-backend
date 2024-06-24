#!/usr/bin/env python3
"""
0. Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This is a helper function that returns the start index and
    end index to determine the pagination parameters

    Parameters
    ----------
    page: int
    pagex_size: int

    Returns
    -------
    A tuple of size two contaitning start index and end index
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size

    return start_index, end_index
