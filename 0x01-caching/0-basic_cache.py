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
        super().__init__()

    def put(self, key: str, item: Any) -> None:
        if key and item:
            self.cache_data[key] = item

    def get(self, key: str) -> Optional[Any]:
        if key:
            return self.cache_data.get(key)
        return None
