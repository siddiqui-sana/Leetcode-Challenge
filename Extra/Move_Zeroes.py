class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Brute Force - Time and Space: O(n) and O(n)
        numZ = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                numZ += 1
        ans = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(nums[i])
        while numZ:
            ans.append(0)
            numZ -= 1
        for i in range(len(nums)):
            nums[i] = ans[i]
        return nums

        # Optimal - Time and Space: O(n), O(1)
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
        return nums

        # More Optimal - Time and Space: O(n), O(n)
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
