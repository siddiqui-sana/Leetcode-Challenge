class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = [0]*32
        neg = 0
        for i in range(32):
            for j in range(len(nums)):
                if nums[j] < 0:
                    nums[j] = abs(nums[j])
                    neg += 1
                if (nums[j] & (1 << i)) != 0:
                    count[i] += 1
        add = 0
        for i in range(32):
            add += (count[i] % 3)*(1 << i)
        if neg % 3 != 0:
            add = -add
        return add
