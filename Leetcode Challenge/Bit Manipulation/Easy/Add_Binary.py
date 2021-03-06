# 1st Approach:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        carry = 0
        add = 0
        ans = []
        while i >= 0 or j >= 0:
            if i >= 0:
                add = add + int(a[i])
            if j >= 0:
                add = add + int(b[j])
            carry = add//2
            ans.append((add % 2))
            add = carry
            i = i-1
            j = j-1
        if carry != 0:
            ans.append(carry)
        return "".join(map(str, ans[::-1]))

# 2nd Approach:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        carry = 0
        res = ""
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            res += str(carry % 2)
            carry //= 2
        return res[::-1]
