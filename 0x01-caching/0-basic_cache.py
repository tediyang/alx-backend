#!/usr/bin/env python3
"""
    A class for basic cache system
"""
from typing import Any, Optional
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        A Class that implements a basic caching system

        Args:
            BaseCaching (class): Base cache model
    """
    def __init__(self) -> None:
        """
            initialize the base
        """
        super().__init__()

    def put(self, key: str, item: Any) -> None:
        """
            add data to the cache dict.

            Args:
                key (str): string key
                item (Any): any data type
        """
        if key and item:
            self.cache_data[key] = item

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
