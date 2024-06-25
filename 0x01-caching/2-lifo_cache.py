#!/usr/bin/env python3
"""
2. LIFO Caching
"""
from base_caching import BaseCaching
from typing import Union, Any


class LIFOCache(BaseCaching):
    """
    LIFO Cache system for storing data in memory evicts the most
    recently added block, i.e Last in first out

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
        self.lifo = []

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
                if len(set(self.lifo)) < BaseCaching.MAX_ITEMS:
                    self.lifo.append(key)
                else:
                    print('DISCARD: {}'.format(self.lifo[-1]))
                    del self.cache_data[self.lifo[-1]]
                    self.lifo[-1] = key
            else:
                self.lifo.remove(key)
                self.lifo.append(key)
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
