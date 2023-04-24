#!/usr/bin/env python3
""" basic cache """

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """basic cache class"""
    def put(self, key, item):
        """put method"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        if key in self.cache_data:
            return self.cache_data[key]
        return None