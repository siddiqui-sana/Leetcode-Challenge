def redu(num, steps):
    if num == 0:
        return steps
    if num % 2 == 0:
        return redu(num//2, steps+1)
    return redu(num-1, steps+1)

class Solution:
    def numberOfSteps(self, num: int) -> int:
        return redu(num, 0)
