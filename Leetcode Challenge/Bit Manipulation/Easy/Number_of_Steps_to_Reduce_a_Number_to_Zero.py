class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        c = 0
        while num > 0:
            if num & 1 == 0:
                num //= 2
            else:
                num -= 1
            c += 1
        return c
