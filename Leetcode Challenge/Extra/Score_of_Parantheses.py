class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Approach 1:
        stck = [0]
        for brac in s:
            if brac == "(":
                stck.append(0)
            else:
                fir = stck.pop()
                sec = stck.pop()
                stck.append(sec+max(2*fir, 1))
        return stck.pop()

        # Approach 2:
        stck = [0]
        scre = 0
        for brac in s:
            if brac == "(":
                stck.append(0)
            else:
                fir = stck.pop()
                stck[-1] += max(2*fir, 1)
        return stck.pop()