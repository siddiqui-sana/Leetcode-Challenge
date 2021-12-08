class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        ele1 = arr1[0]
        ele2 = arr2[0]
        for i in range(1, len(arr1)):
            ele1 = ele1 ^ arr1[i]
        for j in range(1, len(arr2)):
            ele2 = ele2 ^ arr2[j]
        return ele1 & ele2
