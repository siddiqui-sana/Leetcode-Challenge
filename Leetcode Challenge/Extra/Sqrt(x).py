class Solution:
    def mySqrt(self, num: int) -> int:
        start = 0
        end = num
        while start <= end:
            mid = start+(end-start)//2
            if mid*mid == num:
                root = mid
                break
            if mid*mid > num:
                end = mid-1
            else:
                start = mid+1
                root = mid
        return root
