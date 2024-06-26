#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""
import csv
import math
from typing import List, Tuple, Dict, Any, Union


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        if len(self.dataset()) < start:
            return []
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int
                  = 10) -> Dict[str, Union[int, List[List[Any]], None]]:
        """
        This function provide metadata about the request while
        retrieving data from the dataset

        Parameters
        ----------
        page: int
        page_size: int

        Returns
        -------
        A dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous
        page
        total_pages: the total number of pages in the dataset as an
        integer
        """
        if page < 1:
            page = 1
        if page_size < 1:
            return {
                "page_size": 0,
                "page": page,
                "data": [],
                "next_page": None if page * page_size >= len(
                    self.dataset()) else page + 1,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": (len(
                    self.dataset()) + page_size - 1) // page_size
            }

        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info: Dict[str, Union[int, List[List[Any]], None]] = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
