class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # 1st Solution
        res = {}
        for i in range(len(s)-9):
            if s[i:i+10] not in res:
                res[s[i:i+10]] = 0
            res[s[i:i+10]] += 1
        return [key for key, value in res.items() if value > 1]

        # 2nd Solution
        seen = set()
        rep = set()
        for i in range(len(s)-9):
            if s[i:i+10] in seen:
                rep.add(s[i:i+10])
            else:
                seen.add(s[i:i+10])
        return rep
