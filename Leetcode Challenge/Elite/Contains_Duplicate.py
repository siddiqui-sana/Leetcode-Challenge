class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		
		# Time and Space: O(n)
		# 1st Approach:
		hashSet = set()
		for i in range(len(nums)):
			if nums[i] in hashSet:
				return True
			hashSet.add(nums[i])

		# 2nd Approach: 
		hashMap = dict()
		for i in range(len(nums)):
			if nums[i] in hashMap:
				return True
			else:
				hashMap[i] = 1
