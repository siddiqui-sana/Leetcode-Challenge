class Solution:
    def angleClock(self, hr: int, mint: int) -> float:
        # Formula: angle = (30*Hours) - (11/2 * Minutes)
        res = abs(30*hr-5.5*mint)
        if res > 180:
            return 360-res
        return res
