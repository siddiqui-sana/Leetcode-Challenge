class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sArr = [0]*26
        pArr = [0]*26
        res = []
        pLen = len(p)
        sLen = len(s)
        if sLen < pLen:
            return []
        winS = 0
        winE = 0
        while winE < pLen:
            pArr[ord(p[winE])-97] += 1
            sArr[ord(s[winE])-97] += 1
            winE += 1
        winE -= 1
        while winE < sLen:
            if pArr == sArr:
                res.append(winS)
            winE += 1
            if winE != sLen:
                sArr[ord(s[winE])-97] += 1
            else:
                break
            sArr[ord(s[winS])-97] -= 1
            winS += 1
        return res