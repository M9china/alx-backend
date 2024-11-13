#!/usr/bin/python3
""" LRUCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ removes the least recently used items when the limit is reached """

    def __init__(self):
        """ Initialize the LRUCache """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Assigns the item value to the key in the cache_data dictionary.
        If the number of items exceeds BaseCaching.MAX_ITEMS, it discards
        the least recently used item (LRU algorithm).
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update existing item
                self.cache_data[key] = item
                self.usage_order.remove(key)
            else:
                # New item, check for capacity and remove LRU item if necessary
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lru_key = self.usage_order.pop(0)
                    del self.cache_data[lru_key]
                    print(f"DISCARD: {lru_key}")

                self.cache_data[key] = item

            # Add key to end to mark it as most recently used
            self.usage_order.append(key)

    def get(self, key):
        """ Returns the value in cache_data linked to key.
        If key is None or doesn't exist in cache_data, returns None.
        """
        if key is not None and key in self.cache_data:
            # Move key to end to mark it as most recently used
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None


# Example usage:
if __name__ == "__main__":
    my_cache = LRUCache()
    my_cache.put("A", "Apple")
    my_cache.put("B", "Banana")
    my_cache.put("C", "Carrot")
    my_cache.put("D", "Durian")
    print(my_cache.get("A"))

    my_cache.put("E", "Eggplant")
    print(my_cache.get("B"))
    print(my_cache.get("E"))
