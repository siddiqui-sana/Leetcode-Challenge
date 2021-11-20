# 1st Approach:
class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        maxL = -(1 << 31)  # -2147482348
        ones_count = 0
        winS = 0
        for winE in range(len(arr)):
            if arr[winE] == 1:
                ones_count += 1
            if (winE-winS+1)-ones_count > k:
                if arr[winS] == 1:
                    ones_count -= 1
                winS += 1
            maxL = max(maxL, (winE-winS+1))
        return maxL

# 2nd Approach:
class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        winS = 0
        winE = 0
        hashMap = {}
        ones = 0
        maxL = 0
        while winE < len(arr):
            hashMap[arr[winE]] = hashMap.get(arr[winE], 0)+1
            if winE-winS+1-hashMap.get(1, 0) <= k:
                maxL = max(maxL, winE-winS+1)
                winE += 1
            else:
                if hashMap[arr[winS]] == 1:
                    del hashMap[arr[winS]]
                    winS += 1
                    winE += 1
                else:
                    hashMap[arr[winS]] -= 1
                    winS += 1
                    winE += 1
        return maxL
