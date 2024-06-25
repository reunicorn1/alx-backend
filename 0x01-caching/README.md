# 0x01. Caching

Caching is a technique used in computing to store copies of data in high-speed storage systems (caches) so that future requests for that data can be served faster. The data stored in a cache might be the result of an earlier computation or duplicates of data stored elsewhere.
When a cache is full and needs to accommodate new data, it must decide which existing cache item to evict or replace. This decision is guided by cache replacement policies. Here are a few common ones:
Least Recently Used (LRU): This policy replaces the least recently used items first. It assumes that an item used recently will likely be used again soon.
Most Recently Used (MRU): This policy replaces the most recently used items first. It's useful in situations where the older an item is, the more likely it is to be accessed.
Least Frequently Used (LFU): This policy replaces the least frequently used items first. It uses frequency as the criteria for replacement.
Random Replacement (RR): This policy randomly selects a candidate item and replaces it.
Each of these policies has its own strengths and weaknesses, and the choice of policy can greatly affect the performance of the cache.

## Tasks/Files

|    Tasks       |     Files                     |
|----------------|-------------------------------|
|0. Basic dictionary|``0-basic_cache.py``|
|1. FIFO caching|`1-fifo_cache.py`|
|2. LIFO Caching|`2-lifo_cache.py`|
|3. LRU Caching|`3-lru_cache.py`|
|4. MRU Caching|`4-mru_cache.py`|
