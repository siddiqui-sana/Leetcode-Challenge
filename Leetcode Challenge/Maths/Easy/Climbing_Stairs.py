class Solution:
    def __init__(self):
        self.hashMap = {1: 1, 2: 2}

    def climbStairs(self, n):
        if n not in self.hashMap:
            print("sa")
            self.hashMap[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.hashMap[n]
