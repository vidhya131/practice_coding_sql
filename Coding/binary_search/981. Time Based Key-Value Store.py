from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]

        # find insertion position
        idx = bisect_right(values, (timestamp, chr(127))) - 1

        if idx >= 0:
            return values[idx][1]

        return ""