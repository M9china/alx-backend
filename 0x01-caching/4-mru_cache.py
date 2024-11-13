#!/usr/bin/python3
""" MRUCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """removes the most recently used items when the limit is reached """

    def __init__(self):
        """ Initialize the MRUCache """
        super().__init__()
        self.recent_key = None  # Tracks the most recently used key

    def put(self, key, item):
        """ Assigns the item value to the key in the cache_data dictionary.
        If the number of items exceeds BaseCaching.MAX_ITEMS, it discards
        the most recently used item (MRU algorithm).
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update existing item
                self.cache_data[key] = item
            else:
                # New item, check for capacity and remove MRU item if necessary
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    if self.recent_key is not None:
                        del self.cache_data[self.recent_key]
                        print(f"DISCARD: {self.recent_key}")

                self.cache_data[key] = item

            # Update recent_key to the current key (most recently used)
            self.recent_key = key

    def get(self, key):
        """ Returns the value in cache_data linked to key.
        If key is None or doesn't exist in cache_data, returns None.
        """
        if key is not None and key in self.cache_data:
            # Update recent_key to mark this key as the most recently used
            self.recent_key = key
            return self.cache_data[key]
        return None


# Example usage:
if __name__ == "__main__":
    my_cache = MRUCache()
    my_cache.put("A", "Apple")
    my_cache.put("B", "Banana")
    my_cache.put("C", "Carrot")
    my_cache.put("D", "Durian")
    print(my_cache.get("B"))

    my_cache.put("E", "Eggplant")
    print(my_cache.get("B"))
    print(my_cache.get("E"))
