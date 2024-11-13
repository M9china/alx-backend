#!/usr/bin/python3
""" LIFOCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ removes the most recent item added when the limit is reached """

    def __init__(self):
        """ Initialize the LIFOCache """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Assigns the item value to the key in the cache_data dictionary.
        If the number of items exceeds BaseCaching.MAX_ITEMS, it discards
        the most recent item added (LIFO algorithm).
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update existing item
                self.cache_data[key] = item
            else:
                # Add new item and check for capacity
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    if self.last_key is not None:
                        del self.cache_data[self.last_key]
                        print(f"DISCARD: {self.last_key}")

                self.cache_data[key] = item
            # Update last key to be the most recently added/updated key
            self.last_key = key

    def get(self, key):
        """ Returns the value in cache_data linked to key.
        If key is None or doesn't exist in cache_data, returns None.
        """
        return self.cache_data.get(key)


# Example usage:
if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Apple")
    my_cache.put("B", "Banana")
    my_cache.put("C", "Carrot")
    my_cache.put("D", "Durian")
    print(my_cache.get("A"))

    my_cache.put("E", "Eggplant")
    print(my_cache.get("D"))
    print(my_cache.get("E"))
