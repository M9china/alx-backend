#!/usr/bin/python3
""" FIFOCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ removes the oldest items first (FIFO) """

    def __init__(self):
        """ Initialize the FIFOCache """
        super().__init__()
        self.keys_order = []  # List to keep track of the order of insertion

    def put(self, key, item):
        """ Assigns the item value to the key in the cache_data dictionary.
        If the number of items exceeds BaseCaching.MAX_ITEMS, it discards
        the first item added (FIFO algorithm).
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                # New key, check if we need to evict the oldest item
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    oldest_key = self.keys_order.pop(0)
                    del self.cache_data[oldest_key]
                    print(f"DISCARD: {oldest_key}")

            # Add or update the key with its value
            self.cache_data[key] = item
            if key not in self.keys_order:
                self.keys_order.append(key)
            else:
                # Move existing key to end (maintain FIFO order)
                self.keys_order.remove(key)
                self.keys_order.append(key)

    def get(self, key):
        """ Returns the value in cache_data linked to key.
        If key is None or doesn't exist in cache_data, returns None.
        """
        return self.cache_data.get(key)


# Example usage:
if __name__ == "__main__":
    my_cache = FIFOCache()
    my_cache.put("A", "Apple")
    my_cache.put("B", "Banana")
    my_cache.put("C", "Carrot")
    my_cache.put("D", "Durian")
    print(my_cache.get("A"))

    my_cache.put("E", "Eggplant")
    print(my_cache.get("A"))
    print(my_cache.get("E"))
