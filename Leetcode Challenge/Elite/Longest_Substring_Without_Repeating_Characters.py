class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = -(1 << 31)
        winS = 0
        hashMap = {}
        for winE in range(len(s)):
            char = s[winE]
            if char in hashMap:
                winS = max(winS, hashMap[char]+1)
            hashMap[char] = winE
            maxL = max(maxL, winE-winS+1)
        return maxL
