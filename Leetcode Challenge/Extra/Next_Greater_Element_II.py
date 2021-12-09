class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stck = []
        for i in range(n-2, -1, -1):
            while len(stck) != 0 and nums[i] >= stck[-1]:
                stck.pop()
            stck.append(nums[i])
        res = []
        for i in range(n-1, -1, -1):
            while len(stck) != 0 and nums[i] >= stck[-1]:
                stck.pop()
            if len(stck) == 0:
                res.append(-1)
            else:
                res.append(stck[-1])
            stck.append(nums[i])
        res.reverse()
        return res