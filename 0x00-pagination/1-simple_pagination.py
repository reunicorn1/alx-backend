#!/usr/bin/env python3
"""
1. Simple pagination
"""
import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This function returns the approperite page of dataset

        Parameters
        ----------
        page: int
        page_size: int

        Returns
        -------
        a page of the dataset as a list of rows
        """
        self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        if len(self.__dataset) < end:
            return []
        return self.__dataset[start: end]
