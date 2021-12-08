class Solution:
    def isPerfectSquare(self, num: int) -> bool:
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
        if root*root == num:
            return True
        return False
