import math


class Solution:
    def findComplement(self, num: int) -> int:
        # 1st Solution:

        res = 0
        while res < num:
            res = res*2+1
        return res ^ num

        # 2nd Solution:

        dig = math.floor(math.log2(num))+1
        mask = (1 << dig)-1
        return num ^ mask