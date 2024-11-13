#!/usr/bin/python3
""" LFUCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """removes the least frequently used items when the limit is reached """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.frequency = {}  # Tracks the frequency of access for each key
        self.recent_keys = {}  # Tracks the order of access for each key

    def put(self, key, item):
        """ Assigns the item value to the key in the cache_data dictionary.
        If the number of items exceeds BaseCaching.MAX_ITEMS, it discards
        the least frequently used item, using LRU to break ties.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update value and frequency
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            # New key
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Determine which key to remove
                min_freq = min(self.frequency.values())
                # Get all keys with the minimum frequency
                least_used = [
                    k for k, v in self.frequency.items() if v == min_freq
                    ]

                # If there are multiple keys with the same frequency, use LRU
                if len(least_used) > 1:
                    lru_key = min(least_used,
                                  key=lambda k: self.recent_keys[k])
                else:
                    lru_key = least_used[0]

                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.recent_keys[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add new key
            self.cache_data[key] = item
            self.frequency[key] = 1

        # Update recent usage order (LRU for tie-breaking)
        self.recent_keys[key] = self._get_next_order()

    def get(self, key):
        """ Returns the value in cache_data linked to key.
        If key is None or doesn't exist in cache_data, returns None.
        """
        if key is not None and key in self.cache_data:
            # Update frequency and recent access order
            self.frequency[key] += 1
            self.recent_keys[key] = self._get_next_order()
            return self.cache_data[key]
        return None

    def _get_next_order(self):
        """ helps track the least recently used key for tie-breaking """
        return len(self.recent_keys) + 1


# Example usage:
if __name__ == "__main__":
    my_cache = LFUCache()
    my_cache.put("A", "Apple")
    my_cache.put("B", "Banana")
    my_cache.put("C", "Carrot")
    my_cache.put("D", "Durian")
    print(my_cache.get("B"))

    my_cache.put("E", "Eggplant")
    print(my_cache.get("A"))
    print(my_cache.get("E"))
