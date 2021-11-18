class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start+(end-start+1)//2
            if nums[mid] == target:
                start = mid
                end = mid
                while start > 0 and nums[start-1] == target:
                    start -= 1
                while end < len(nums) and nums[end+1] == target:
                    end += 1
                return [start, end]
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return [-1, -1]
