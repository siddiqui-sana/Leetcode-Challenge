class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Approach 1:
        # Will give you the TLE error...
        res = []

        def permu(n, till):
            if len(n) == 0:
                res.append(till)
                return res
            for i in range(len(n)):
                ch = n[i]
                left = n[:i]
                right = n[i+1:]
                rest = left+right
                permu(rest, till+ch)
            return res
        return permu(list(map(str, range(1, n+1))), "")[k-1]

        # Approach 2:
        # Optimal Solution:
        # Removal of list element: O(n)
        # Time: O(n)*O(n)
        # Space: O(n)
        fact = 1
        digits = []
        for i in range(1, n):
            fact *= i
            digits.append(i)
        digits.append(n)
        k -= 1
        res = ""
        while True:
            index = k//fact
            res += str(digits[index])
            del digits[index]
            if len(digits) == 0:
                break
            k = k % fact
            fact = fact//len(digits)
        return res
