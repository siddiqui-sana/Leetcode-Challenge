# Brute Force - O(n)  - TLE
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum % k == 0:
                    count += 1
        return count

# Optimal Approach - Time and Space: O(n), O(n)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = {0: 1}
        prefSum = 0
        count = 0
        for i in range(len(nums)):
            prefSum = (prefSum + nums[i]) % k
            if prefSum < 0:
                prefSum += k
            if prefSum in res:
                count += res[prefSum]
            if prefSum not in res:
                res[prefSum] = 0
            res[prefSum] += 1
        return count
