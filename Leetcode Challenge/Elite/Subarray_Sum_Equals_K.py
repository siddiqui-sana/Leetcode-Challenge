class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force - Time: O(n) - (TLE)
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count

        # Using HashTable - Time and Space: O(n) and O(n)
        res = {0: 1}
        prefSum = 0
        count = 0
        for i in range(len(nums)):
            prefSum += nums[i]
            if prefSum-k in res:
                count += res[prefSum-k]
            if prefSum not in res:
                res[prefSum] = 0
            res[prefSum] += 1
        return count
