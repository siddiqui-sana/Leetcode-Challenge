class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stck = []
        nsel = []
        for i in range(0, len(heights)):
            while(len(stck) != 0 and heights[stck[-1]] >= heights[i]):
                stck.pop()

            if len(stck) == 0:
                nsel.append(-1)

            else:
                nsel.append(stck[-1])

            stck.append(i)
        stck = []
        nser = []

        for i in range(len(heights) - 1, -1, -1):
            while(len(stck) != 0 and heights[stck[-1]] >= heights[i]):
                stck.pop()

            if len(stck) == 0:
                nser.append(len(heights))

            else:
                nser.append(stck[-1])

            stck.append(i)
        nser.reverse()
        maxA = 0
        for i in range(len(heights)):
            area = (nser[i]-nsel[i]-1)*heights[i]
            maxA = max(maxA, area)
        return maxA