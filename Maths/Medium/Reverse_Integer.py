# 1st Approach:
class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        if rev.bit_length()>31:
            return 0
        if x<0:
            return -1*rev
        else:
            return rev

# 2nd Approach:
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        res = 0
        while x:
            res = res*10+x % 10
            x //= 10
        return 0 if res > (1 << 31) else res*sign
