#!/usr/bin/env python3
"""
1. FIFO caching
"""
from base_caching import BaseCaching
from typing import Union, Any


class FIFOCache(BaseCaching):
    """
    FIFO Cache system for storing data in memory evicts blocks from
    cache in their order of arrival

    Attributes
    ----------
    cache_data: A dictionary from the parent class BaseCaching

    Methods
    ------
    put: (key, item)
        saves a new item inside the cache system
    get: (key)
        returns an item from the cache
    """
    def __init__(self):
        """
        The constructor for the FIFO Cache class.
        """
        super().__init__()
        self.fifo = []
        self.last = 0

    def put(self, key: Union[int, str, None], item: Any):
        """
        Assigns the dictionary self.cache_data the item value
        for the key

        Parameters
        ----------
        key: str, int
        item: Any

        Returns
        -------
        None
        """
        if key and item:
            if not self.cache_data.get(key):
                if len(self.fifo) < BaseCaching.MAX_ITEMS:
                    self.fifo.append(key)
                else:
                    print('DISCARD: {}'.format(self.fifo[self.last]))
                    del self.cache_data[self.fifo[self.last]]
                    self.fifo[self.last] = key
                    self.last = (self.last + 1) % BaseCaching.MAX_ITEMS
            self.cache_data[key] = item

    def get(self, key: Union[str, int, None]) -> Any:
        """
        Returns an item back from the cache

        Parameters
        ----------
        key: Any

        Returns
        -------
        the value of the key or None
        """
        return self.cache_data.get(key)
