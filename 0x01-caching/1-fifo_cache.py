#!/usr/bin/env python3
"""
    A class that applies FIFO Caching system
"""
from typing import Any, Optional
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        A class that uses first in first out for caching

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self) -> None:
        """
            initialize the base
        """
        super().__init__()

    def put(self, key: str, item: Any) -> None:
        """
            a function that adds data to the cache dict.

            Args:
                key (str): key of data
                item (Any): value to be saved
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                first = sorted(self.cache_data.keys())[0]
                self.cache_data.pop(first)
                print("DISCARD: ", format(first))

    def get(self, key: str) -> Optional[Any]:
        """
            get the data with the provided key.

            Args:
                key (str): the key

            Returns:
                Optional[Any]: value with any data type
        """
        if key:
            return self.cache_data.get(key)
        return None
