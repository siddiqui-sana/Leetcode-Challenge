class Solution:
    def productExceptSelf(self, nums):
        # Approach 1:
        # Time and Space: O(n) and O(n)
        left, right, res = [], [1]*len(nums), []
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            left.append(prod)
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod *= nums[i]
            right[i] = prod
        res.append(right[1])
        for i in range(1, len(nums)-1):
            res.append(left[i-1]*right[i+1])
        res.append(left[-2])
        return res

        # Approach 2:
        # Time and Space: O(n) and O(1)
        res = []
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            res.append(prod)
        print(res)
        prod = 1
        for i in range(len(nums)-1, 0, -1):
            res[i] = res[i-1]*prod
            prod = prod*nums[i]
        res[0] = prod
        return res
