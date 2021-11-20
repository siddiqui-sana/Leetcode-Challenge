class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = 0
        temp = x
        while temp:
            res = res*10+temp % 10
            temp //= 10
        if x == res:
            return True
        return False

