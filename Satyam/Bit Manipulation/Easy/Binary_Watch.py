class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for hr in range(12):
            for minu in range(60):
                if (bin(hr)+bin(minu)).count("1") == turnedOn:
                    res.append(f"{hr}:{minu:02d}")
        return res