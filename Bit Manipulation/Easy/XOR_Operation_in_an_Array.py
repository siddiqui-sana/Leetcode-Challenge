class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # 1st Solution:

        # res = 0
        # nums = [0]*n
        # for i in range(n):
        #     nums[i] = start+(2*i)
        #     res ^= nums[i]
        # return res

        # 2nd Solution:

        res = 0
        for i in range(n):
            res ^= (start+(2*i))
        return res
