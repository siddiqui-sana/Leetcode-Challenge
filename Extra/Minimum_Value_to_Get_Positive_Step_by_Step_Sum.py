class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            ans = min(ans, sum)
        return -ans+1
