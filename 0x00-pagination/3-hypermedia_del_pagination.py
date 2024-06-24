#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
from typing import List, Dict, Optional
import csv


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def next_index(self, index: Optional[int], jump: int = 1) -> Optional[int]:
        """Gets the next index after a certain count
        """
        if index is None:
            return None

        start = index
        while jump:
            while not self.__indexed_dataset.get(start):
                start += 1
                if start >= len(self.__dataset):
                    return None
                print(start)
            jump -= 1
            start += 1
        print('end§:')
        return start

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """
        This function returns metadata about the paginated dataset
        to help clients request for the next page and also giving them
        information about their current request

        Parameters
        ----------
        index: Optional[int]
            the start index of your query
        page_size: int
            the size of the requested dataset

        Returns
        -------
        A dictionary with the following key-value pairs:
        index: Optional[int]
            the current start index of the return page.
        next_index: Optional[int]
            the next index to query with.
        page_size: int
            the current page size
        data: List[List[str]]
            the actual page of the dataset
        """
        assert isinstance(page_size, int)
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0 and index < len(
                self.__dataset)
        data = []
        idx: Optional[int] = index
        for _ in range(page_size):
            if idx is None:
                break
            while not self.__indexed_dataset.get(idx) and idx < len(
                    self.__dataset):
                idx += 1
            if idx >= len(self.__dataset):
                break
            data.append(self.__indexed_dataset.get(idx))
            idx += 1

        return {
            'index': index,
            'next_index': self.next_index(index, page_size),
            'page_size': len(data),
            'data': data
        }
