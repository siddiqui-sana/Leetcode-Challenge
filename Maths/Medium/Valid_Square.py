class Solution:
    def dist(self, tup1, tup2):
        x1, y1 = tup1
        x2, y2 = tup2
        return (((x2-x1)**2)+((y2-y1)**2))**0.5
        # x**0.5 = math.sqrt(x)

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        edges = [(p1, p2), (p1, p3), (p1, p4), (p2, p3), (p2, p4), (p3, p4)]
        edges_occ = [self.dist(i, j) for i, j in edges]
        count = Counter(edges_occ).most_common()
        if len(count) != 2:
            return False
        return (count[0][1] == 4 and count[1][1] == 2) and (int(count[1][0]) == (int(count[0][0]*(2**0.5))))
        # (2**0.5) = math.sqrt(2)
