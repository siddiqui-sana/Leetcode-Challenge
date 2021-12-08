class Solution:
    def myAtoi(self, s: str) -> int:
        s = list(s.strip())
        if len(s) == 0:
            return 0
        sign = -1 if s[0] == "-" else 1
        if s[0] in ["-", "+"]:
            del s[0]
        i = 0
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res*10 + (ord(s[i])-ord('0'))
            i += 1
        # You can also write the below code for returning the result
        return max((-(1 << 31)), min(res*sign, (1 << 31)-1))

        # or

        if res*sign < -(1 << 31):
            return -(1 << 31)
        elif res*sign > (1 << 31)-1:
            return (1 << 31)-1
        else:
            return res*sign
