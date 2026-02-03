import time

CACHE_TTL_SECONDS = 3600  # 1 hora

class DecisionCache:
    def __init__(self):
        # key -> (value, timestamp)
        self.data = {}

    def get(self, key):
        entry = self.data.get(key)
        if not entry:
            return None

        value, timestamp = entry

        # expirou
        if time.time() - timestamp > CACHE_TTL_SECONDS:
            del self.data[key]
            return None

        return value

    def set(self, key, value):
        self.data[key] = (value, time.time())

    def stats(self):
        now = time.time()
        valid = sum(
            1 for _, (_, ts) in self.data.items()
            if now - ts < CACHE_TTL_SECONDS
        )

        return {
            "entries_total": len(self.data),
            "entries_valid": valid,
            "ttl_seconds": CACHE_TTL_SECONDS
        }
