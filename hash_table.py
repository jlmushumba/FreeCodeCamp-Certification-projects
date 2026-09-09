class HashTable:
    def __init__(self):
        self.collection = {}
    def hash(self, string: str):
        return sum(ord(char) for char in string)
        
    def add(self, key, value):
        hash_key = self.hash(key)
        if  not hash_key in self.collection:
            self.collection[hash_key] = {}
        
        self.collection[hash_key][key] = value
            

        
    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                del self.collection[hash_key][key]

          
            
    def lookup(self, key):
        hash_key = self.hash(key)
        
        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                return self.collection[hash_key][key]
