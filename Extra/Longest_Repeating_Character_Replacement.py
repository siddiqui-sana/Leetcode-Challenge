# 1st Approach:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        winS = 0
        winE = 0
        hashMap = {}
        maxL = 0

        def solve(hashMap):
            value = hashMap.values()
            return max(value)
        while winE < len(s):
            hashMap[s[winE]] = hashMap.get(s[winE], 0)+1
            if len(hashMap) == 1:
                maxL = max(maxL, winE-winS+1)
                winE += 1
            else:
                if winE-winS+1-solve(hashMap) <= k:
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
    def characterReplacement(self, s: str, k: int) -> int:
        winS = 0
        maxL = -(1 << 31)  # 2147483648
        maxChar = 0
        freq = {}
        for winE in range(len(s)):
            freq[s[winE]] = freq.get(s[winE], 0)+1
            maxChar = max(maxChar, freq[s[winE]])
            if ((winE-winS+1)-(maxChar)) > k:
                if freq[s[winS]] == 1:
                    del freq[s[winS]]
                else:
                    freq[s[winS]] -= 1
                winS += 1
            maxL = max(maxL, winE-winS+1)
        return maxL

# 3rd Approach:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        winS = 0
        winE = 0
        hashMap = {}
        maxL = 0

        def solve(hashMap):
            res = sorted(hashMap.values(), reverse=True)
            return sum(res[1:])
        while winE < len(s):
            hashMap[s[winE]] = hashMap.get(s[winE], 0)+1
            if len(hashMap) == 1:
                maxL = max(maxL, winE-winS+1)
                winE += 1
            else:
                if solve(hashMap) <= k:
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
