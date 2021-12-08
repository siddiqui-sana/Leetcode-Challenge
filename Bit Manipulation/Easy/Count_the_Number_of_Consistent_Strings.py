# class Solution:
#     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#         count = len(words)
#         for word in words:
#             for w in word:
#                 if w not in allowed:
#                     count -= 1
#                     break
#         return count


