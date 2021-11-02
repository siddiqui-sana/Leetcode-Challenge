class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n > 1:
            bit1 = n & 1
            n >>= 1
            bit2 = n & 1
            if bit1 == bit2:
                return False
        return True
