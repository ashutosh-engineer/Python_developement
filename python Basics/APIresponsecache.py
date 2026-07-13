'''
Build create_cache(ttl_seconds) jo ek fetch(key, compute_fn) function return kare.
Requirements:

Agar key cache mein hai aur TTL expire nahi hua — cached value return karo
Agar nahi hai ya expire ho gaya — compute_fn() call karo, result store karo, return karo
Track karo: total hits, total misses, total expired
fetch pe ek attribute get_stats() function attach karo jo stats return kare

Test karna hai:
cache = create_cache(ttl_seconds=2)

result1 = cache("user_1", lambda: "data_from_db")
result2 = cache("user_1", lambda: "data_from_db")  # should hit cache
time.sleep(3)
result3 = cache("user_1", lambda: "fresh_data")    # TTL expired

print(cache.get_stats())
# {"hits": 1, "misses": 1, "expired": 1}
'''

import time

def create_cache(ttl_seconds):
    cache = {}
    hits = 0
    misses = 0
    expired = 0

    def fetch(key, compute_fn):
        nonlocal hits, misses, expired

        if key not in cache:
            result = compute_fn()
            cache[key] = {"value": result, "stored_at": time.time()}
            misses += 1
            return result

        else:
            if time.time() - cache[key]["stored_at"] > ttl_seconds:
                expired += 1
                result = compute_fn()
                cache[key] = {"value": result, "stored_at": time.time()}
                return result
            else:
                hits += 1
                return cache[key]["value"]

    def get_stats():
        return {"hits": hits, "misses": misses, "expired": expired}

    fetch.get_stats = get_stats
    return fetch