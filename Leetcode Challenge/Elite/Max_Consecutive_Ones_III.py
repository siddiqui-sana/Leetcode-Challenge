class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        maxL = -(1 << 31)
        ones = 0
        ws = 0
        for we in range(len(arr)):
            if arr[we] == 1:
                ones += 1
            if (((we-ws+1)-(ones)) > k):
                if arr[ws] == 1:
                    ones -= 1
                ws += 1
            maxL = max(maxL, we-ws+1)
        return maxL
