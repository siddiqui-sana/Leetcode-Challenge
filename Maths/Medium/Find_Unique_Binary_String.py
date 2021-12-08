class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        bit = 1 << len(nums[0])
        bitLen = len(nums[0])
        res = [i for i in range(bit)]
        for i in range(len(nums)):
            nums[i] = int(nums[i], 2)
        res = [num for num in res if num not in nums]
        bit = len(bin(res[0])[2:])
        if bit != bitLen:
            return (bitLen-bit)*"0"+bin(res[0])[2:]
        return bin(res[0])[2:]