class Solution:
    def angleClock(self, hr: int, mint: int) -> float:
        res = abs(30*hr-5.5*mint)
        if res > 180:
            return 360-res
        return res