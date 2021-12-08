class Solution:
    def guessNumber(self, n: int) -> int:
        s = 0
        e = n
        while s <= e:
            mid = s+(e-s)//2
            temp = guess(mid)
            if temp == 0:
                return mid
            elif temp < 0:
                e = mid-1
            else:
                s = mid+1
        return -1
