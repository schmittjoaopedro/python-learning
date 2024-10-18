import random

class RandomizedSet:

    def __init__(self):
        self.numToIdx = {}
        self.nums = []
        self.length = 0


    def insert(self, val: int) -> bool:
        if val in self.numToIdx:
            return False
        else:
            if self.length == len(self.nums):
                self.nums.append(0)
            self.nums[self.length] = val
            self.numToIdx[val] = self.length
            self.length += 1
            return True


    def remove(self, val: int) -> bool:
        if val not in self.numToIdx:
            return False
        else:
            idx = self.numToIdx[val]
            self.nums[idx] = self.nums[self.length-1]
            self.numToIdx[self.nums[idx]] = idx
            del self.numToIdx[val]
            self.length -= 1
            return True


    def getRandom(self) -> int:
        rnd = random.randint(0, self.length - 1)
        return self.nums[rnd]
