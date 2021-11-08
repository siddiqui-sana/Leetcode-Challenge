class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def solve(s):
            if len(s) < 2:
                return ""
            res = []
            for ind, val in enumerate(s):
                if val.isupper() and val.lower() not in s:
                    res.append(ind)
                if val.islower() and val.upper() not in s:
                    res.append(ind)
            if len(res) == 0:
                return s
            else:
                mid = len(res)//2
                return max(solve(s[:res[mid]]), solve(s[res[mid]+1:]), key=len)

        return solve(s)