class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        three = n//3
        rem = n % 3
        if rem == 0:
            return 3**three
        elif rem == 1:
            return (3**(three-1))*4
        else:
            return (3**three)*2

# 6 = 3x3 = 9
# 7 = 3x4 = 12
# 8 = 3x3x2 = 18
# 9 = 3x3x3 = 27
# 10 = 3x3x4 = 36
# 54 = 3 ^ 18 = 387420489
# 55 = (3 ^ 17)*4 = 516560652
# 56 = (3 ^ 18)*2 = 774840978
