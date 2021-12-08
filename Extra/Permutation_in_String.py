class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sArr = [0]*26
        pArr = [0]*26
        pLen = len(s1)
        sLen = len(s2)
        if sLen < pLen:
            return False
        winS = 0
        winE = 0
        while winE < pLen:
            pArr[ord(s1[winE])-97] += 1
            sArr[ord(s2[winE])-97] += 1
            winE += 1
        winE -= 1
        while winE < sLen:
            if pArr == sArr:
                return True
            winE += 1
            if winE != sLen:
                sArr[ord(s2[winE])-97] += 1
            else:
                break
            sArr[ord(s2[winS])-97] -= 1
            winS += 1
        return False