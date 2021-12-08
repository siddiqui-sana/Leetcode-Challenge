class Solution:
    def binaryGap(self, n: int) -> int:
        flag = 0
        maxDis = 0
        dis = 0
        while n > 0:
            if n & 1:
                flag = 1
                maxDis = max(maxDis, dis)
                dis = 1
            elif flag == 1:
                dis += 1
            n >>= 1
        return maxDis