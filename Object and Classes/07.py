class DataCache:
    def __init__ (self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.list = deque(maxlen=self.capacity)

    def get(self, key):
        self.list.remove(key)
        self.list.append(key)
        return self.dict[key]
    
    def put(self, key, data):
        if key in self.dict:
            self.dict[key] = data
            self.list.remove(key)
            self.list.append(key)
        elif len(self.dict) < self.capacity:
            self.dict[key] = data
            self.list.append(key)
        else:
            del self.dict[self.list[0]]
            self.dict[key] = data
            self.list.append(key)