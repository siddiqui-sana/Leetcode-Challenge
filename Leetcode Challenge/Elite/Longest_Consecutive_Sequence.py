class Solution:
    def longestConsecutive(self, nums):
        # Brute Force: O(n^2)
        maxL = -(1 << 31)
        for num in nums:
            curN = num
            curS = 1
            while curN+1 in nums:
                curN += 1
                curS += 1
            maxL = max(maxL, curS)
        return maxL

        # Efficient: O(n)
        if not nums:
            return 0
        hashSet = set(nums)
        maxL = -(1 << 31)
        for num in hashSet:
            if num-1 not in hashSet:
                curN = num
                curS = 1
                while curN+1 in hashSet:
                    curN += 1
                    curS += 1
                maxL = max(maxL, curS)
        return maxL
