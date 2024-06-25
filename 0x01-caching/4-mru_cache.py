#!/usr/bin/env python3
"""
4. MRU Caching
"""
from base_caching import BaseCaching
from typing import Union, Any


class MRUCache(BaseCaching):
    """
    MRU Cache system for storing data. Evicts most recently referred
    block. Works well with cyclic patterns.

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
        self.mru = []

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
            if self.cache_data.get(key):
                self.mru.remove(key)
                self.mru.append(key)
            else:
                if len(self.mru) < BaseCaching.MAX_ITEMS:
                    self.mru.append(key)
                else:
                    print('DISCARD: {}'.format(self.mru[-1]))
                    del self.cache_data[self.mru[-1]]
                    del self.mru[-1]
                    self.mru.append(key)
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
        item = self.cache_data.get(key)
        if item:
            self.mru.remove(key)
            self.mru.append(key)
        return item
