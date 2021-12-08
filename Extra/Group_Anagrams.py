# Note: Must do the Question, Valid Anagram, before it!
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # With Sorting:
        hashMap = {}
        for anag in strs:
            key = "".join(sorted(anag))
            if key in hashMap.keys():
                hashMap[key].append(anag)
            else:
                hashMap[key] = []
                hashMap[key].append(anag)
        return list(hashMap.values())

        # Without Sorting
        hashMap = {}
        for anag in strs:
            res = [0]*26
            for char in anag:
                res[ord(char)-ord('a')] += 1  # Concept of Valid Anagrams
            res = tuple(res)
            if res in hashMap:
                hashMap[res].append(anag)
            else:
                hashMap[res] = [anag]
        return list(hashMap.values())
