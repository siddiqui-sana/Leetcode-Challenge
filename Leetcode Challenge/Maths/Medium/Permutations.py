class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permu(nums, till):
            if len(nums) == 0:
                res.append(till)
                return res
            for i in range(len(nums)):
                ch = nums[i]
                left = nums[:i]
                right = nums[i+1:]
                rest = left+right
                permu(rest, till+[ch])
            return res
        return permu(nums, [])
