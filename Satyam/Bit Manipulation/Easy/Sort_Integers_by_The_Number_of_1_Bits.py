class Solution:
    def countBits(self, n):
        c = 0
        while n > 0:
            if n & 1:
                c += 1
            n >>= 1
        return c

    def sortByBits(self, arr: List[int]) -> List[int]:
        res = {}
        arr.sort()
        for i in range(len(arr)):
            bits = self.countBits(arr[i])
            if res.get(bits):
                res[bits].append(arr[i])
            else:
                res[bits] = [arr[i]]
        ans = []
        for i in range(15):  # Since we have only 14 bits (10^4)
            if res.get(i):
                ans += res[i]
        return ans
