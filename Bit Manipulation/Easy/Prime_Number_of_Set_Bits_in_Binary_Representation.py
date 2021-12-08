class Solution:
    def countBits(self, n):
        c = 0
        while n > 0:
            if n & 1:
                c += 1
            n >>= 1
        return c

    def primeBits(self, n):
        
        # prime = [False, False, True, True, False, True, False, True, False,
        #          False, False, True, False, True, False, False, False, True, False, True]
        # return prime[n]
        
        # OR
        
        if n == 0 or n == 1:
            return False
        for i in range(2, (n//2)+1):
            if n % i == 0:
                return False
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1, 1):
            if self.primeBits(self.countBits(i)):
                count += 1
        return count