# 1st Approach:
class Solution:
	def maxVowels(self, s: str, k: int) -> int:
		sLen = len(s)
		winS = 0
		winE = 0
		vowels = ['a', 'e', 'i', 'o', 'u']
		vCount = 0
		while winE < k:
			if s[winE] in vowels:
				vCount += 1
			winE += 1
		winE -= 1
		maxL = vCount
		while winE < sLen-1:
			if s[winS] in vowels:
				vCount -= 1
			winS += 1
			winE += 1
			if s[winE] in vowels:
				vCount += 1
			maxL = max(maxL, vCount)
		return maxL

# 2nd Approach: Faster than 99%
class Solution:
	def maxVowels(self, s: str, k: int) -> int:
		vowels = {'a', 'e', 'i', 'o', 'u'}
		maxL = vCount = sum(s[i] in vowels for i in range(k))
		for i in range(k, len(s)):
			if s[i-k] in vowels:
				vCount -= 1
			if s[i] in vowels:
				vCount += 1
				maxL = max(maxL, vCount)

		return maxL