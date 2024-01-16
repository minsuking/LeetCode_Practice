from collections import defaultdict
class RandomizedSet:

    def __init__(self):
        self.repository = dict()

    def insert(self, val: int) -> bool:
        if val in self.repository:
            return False
        self.repository[val] = 1
        return True
    
    def remove(self, val: int) -> bool:
        if val in self.repository:
            del self.repository[val]
            return True
        return False

    def getRandom(self) -> int:
        keyList = list(self.repository.keys())
        return random.choice(keyList)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()