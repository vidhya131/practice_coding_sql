class TimeMap:

    def __init__(self):
        self.mapp = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapp[key] = (value, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        prev_timestamp = self.mapp.get(key)[1]
        if timestamp >= prev_timestamp:
            return self.mapp.get(key)[0]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)