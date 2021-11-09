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
