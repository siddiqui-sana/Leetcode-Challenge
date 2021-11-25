class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def find(target, points):
            res, final, count = {}, 0, 0
            x1, y1 = target
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                ans = (x2-x1)/(y2-y1) if y2 != y1 else "inf"
                count = res.get(ans, 0)+1
                res[ans] = count
                final = max(final, count)
            return final+1

        ans = 0
        for x1, y1 in points:
            ans = max(ans, find((x1, y1), points))
        return ans