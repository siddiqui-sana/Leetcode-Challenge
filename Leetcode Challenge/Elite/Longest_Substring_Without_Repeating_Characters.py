# 1st Approach:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        winS = winE = 0
        hashMap = {}
        maxL = 0
        while winE < len(s):
            hashMap[s[winE]] = hashMap.get(s[winE], 0)+1
            if len(hashMap) == winE-winS+1:
                maxL = max(maxL, winE-winS+1)
                winE += 1
            else:
                if hashMap[s[winS]] == 1:
                    del hashMap[s[winS]]
                    winS += 1
                    winE += 1
                else:
                    hashMap[s[winS]] -= 1
                    winS += 1
                    winE += 1
        return maxL


# 2nd Approach:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        winS = 0
        hashMap = {}
        for winE in range(len(s)):
            char = s[winE]
            if char in hashMap:
                winS = max(winS, hashMap[char]+1)
            hashMap[char] = winE
            maxL = max(maxL, winE-winS+1)
        return maxL
