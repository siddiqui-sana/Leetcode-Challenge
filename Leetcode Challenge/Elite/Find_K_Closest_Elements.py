Using Heap:
import heapq
class Solution(object):
    # Time: O(nlogn), Space: O(n)
    def findClosestElements(self, arr, k, x):
        heap = []
        res = []
        # nlogn
        for i in range(len(arr)):  # n
            heap.append((abs(x-arr[i]), arr[i]))
        # heapify() - logn
        # Means smallest at the first position - all times...
        heapq.heapify(heap)
        # nlogn
        for _ in range(k):  # n
            # heappop() - logn
            # Append the values accordingly...
            res.append(heapq.heappop(heap)[1])
        return sorted(res)  # nlogn


# Using Binary Search:
class Solution(object):
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        low = 0
        high = n-1
        while low <= high:
            mid = low+(high-low)//2
            if arr[mid] == x:
                break
            elif arr[mid] < x:
                low = mid+1
            else:
                high = mid-1
        if mid == 0:
            low = mid
            high = mid+1
        else:
            low = mid-1
            high = mid
        res = []
        while k > 0 and low >= 0 and high < n:
            if abs(arr[low]-x) <= abs(arr[high]-x):
                res.append(arr[low])
                low -= 1
            else:
                res.append(arr[high])
                high += 1
            k -= 1
        # For case:
        # arr = [10, 20, 30, 40, 59]
        # x=15
        # k=3
        while k > 0 and low >= 0:
            res.append(arr[low])
            low -= 1
            k -= 1
        # For case:
        # arr = [10, 20, 30, 40, 59]
        # x=25
        # k=3
        while k > 0 and high < n:
            res.append(arr[high])
            high += 1
            k -= 1
        return sorted(res)
