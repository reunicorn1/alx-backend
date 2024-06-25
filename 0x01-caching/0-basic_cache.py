#!/usr/bin/env python3
"""
0. Basic dictionary
"""
from base_caching import BaseCaching
from typing import Union, Any


class BasicCache(BaseCaching):
    """
    BaseCache system for storing data in memory

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
        The constructor for the BaseCache class.
        """
        super().__init__()

    def put(self, key: Union[str, int, None], item: Any) -> None:
        """
        Assigns the dictionary self.cache_data the item value for the
        key

        Parameters
        ----------
        key: str, int
        item: Any

        Returns
        -------
        None
        """
        if key and item:
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
