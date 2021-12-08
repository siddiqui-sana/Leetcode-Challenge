class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        length = 1 << n
        res = []
        for i in range(length):
            temp = []
            for j in range(n):
                if i & (1 << j):
                    temp.append(nums[j])
            if temp not in res:
                res.append(temp)
        return res
