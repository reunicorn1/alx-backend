#!/usr/bin/env python3
"""
5. LFU Caching
"""
from base_caching import BaseCaching
from typing import Union, Any


class LFUCache(BaseCaching):
    """
    LFU Cache system for storing data. The LFU algorithm counts how
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
        self.lfu = []

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
                element = next((t for t in self.lfu if t[0] == key))
                self.lfu.remove(element)
                self.lfu.append((key, element[1] + 1))
            else:
                if len(self.lfu) >= BaseCaching.MAX_ITEMS:
                    element = min(self.lfu, key=lambda x: x[1])
                    print('DISCARD: {}'.format(element[0]))
                    del self.cache_data[element[0]]
                    self.lfu.remove(element)
                self.lfu.append((key, 1))
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
            element = next((t for t in self.lfu if t[0] == key))
            self.lfu.remove(element)
            self.lfu.append((key, element[1] + 1))
        return item
