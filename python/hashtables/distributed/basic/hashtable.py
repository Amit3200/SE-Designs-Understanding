class HashTable:
    def __init__(self):
        self.map = {}
    
    def put(self, key, value):
        self.map[key] = value
    
    def get(self, key):
        if key in self.map:
            return self.map[key]
        return None
    
    def remove(self, key):
        if key in self.map:
            del self.map[key]
            return True
        return None
