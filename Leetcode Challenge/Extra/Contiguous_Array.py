class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashMap = {0: -1}
        add = 0
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                add += -1
            else:
                add += 1
            if add in hashMap:
                maxLen = max(maxLen, i-hashMap[add])
            else:
                hashMap[add] = i
        return maxLen
