class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # 1st Approach - Time: O(nlogn), Space: O(1)
        nums.sort()
        sum = 0
        strt = 0
        end = len(nums)-1
        while strt <= end:
            sum += nums[end]-nums[strt]
            end -= 1
            strt += 1
        return sum

        # 2nd Approach - Time  : O(n)+O(nlogn), Space: O(1)
        nums.sort()
        med = nums[len(nums)//2]
        sum = 0
        for num in nums:
            sum += abs(med-num)
        return sum
