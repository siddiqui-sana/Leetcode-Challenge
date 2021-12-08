# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         # Brute Force:
#         hashMap = {}
#         for i in range(len(nums)):
#             if nums[i] in hashMap:
#                 if abs(i-hashMap[nums[i]]) <= k:
#                     return True
#                 else:
#                     hashMap[nums[i]] = i
#             else:
#                 hashMap[nums[i]] = i

#         # Shrink Above Approach:
#         hashMap = {}
#         for i in range(len(nums)):
#             if nums[i] not in hashMap and abs(i-hashMap[nums[i]]) > k:
#                 hashMap[nums[i]] = i
#             else:
#                 return True



