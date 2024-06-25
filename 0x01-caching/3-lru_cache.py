#!/usr/bin/env python3
"""
3. LRU Caching
"""
from base_caching import BaseCaching
from typing import Union, Any


class LRUCache(BaseCaching):
    """
    LRU Cache system for storing data. The LFU algorithm counts how
    often an item is needed; those used less often are discarded first.

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
        self.lru = []

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
                self.lru.remove(key)
                self.lru.append(key)
            else:
                if len(self.lru) < BaseCaching.MAX_ITEMS:
                    self.lru.append(key)
                else:
                    print('DISCARD: {}'.format(self.lru[0]))
                    del self.cache_data[self.lru[0]]
                    del self.lru[0]
                    self.lru.append(key)
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
            self.lru.remove(key)
            self.lru.append(key)
        return item
