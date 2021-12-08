class Solution:
    def nextLargerElement(self, arr, n):
        stck = []
        res = []
        for i in range(n-1, -1, -1):
            while stck and stck[-1] <= arr[i]:
                stck.pop()
            if not stck:
                res.append(-1)
            else:
                res.append(stck[-1])
            stck.append(arr[i])
        res.reverse()
        return res