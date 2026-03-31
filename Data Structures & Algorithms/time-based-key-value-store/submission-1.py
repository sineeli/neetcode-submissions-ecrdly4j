class TimeMap:

    def __init__(self):
        self.time_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[(key, timestamp)] = value
        

    def get(self, key: str, timestamp: int) -> str:
        for i in range(timestamp, 0, -1):
            if self.time_dict.get((key, i)) is not None:
                return self.time_dict[(key, i)]
        
        return ""
        
