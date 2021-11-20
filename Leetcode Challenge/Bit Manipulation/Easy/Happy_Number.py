class Solution:
    def isHappy(self, n: int) -> bool:
        # Time and Space: O(logn), O(logn)
        def sumi(n):
            res = 0
            while n:
                res += (n % 10)**2
                n //= 10
            return res
        res = set()
        while n != 1 and n not in res:
            res.add(n)
            n = sumi(n)
        return n == 1