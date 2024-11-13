#!/usr/bin/python3
""" BasicCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system with no limit on storage """

    def put(self, key, item):
        """ Assigns the item value to the key in the cache_data dictionary.
        If key or item is None, does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in cache_data linked to key.
        If key is None or doesn't exist in cache_data, returns None.
        """
        return self.cache_data.get(key)


# Example usage:
if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.put("A", "Apple")
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    my_cache.put(None, "Banana")
    print(my_cache.get(None))
