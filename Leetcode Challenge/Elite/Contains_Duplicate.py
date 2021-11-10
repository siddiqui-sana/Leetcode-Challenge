class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time and Space: O(n)
        hashSet = set()
        for i in range(len(nums)):
            if nums[i] in hashSet:
                return True
            hashSet.add(nums[i])