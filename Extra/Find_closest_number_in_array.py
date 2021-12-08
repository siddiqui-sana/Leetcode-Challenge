def findClosest(arr, n, tar):
    # Base/ Corner Cases
    if tar <= arr[0]:
        return arr[0]
    if tar >= arr[n-1]:
        return arr[n-1]
    start = 0
    end = n
    while start <= end:
        mid = start+(end-start)//2
        if tar == arr[mid]:
            return arr[mid]
        if tar < arr[mid]:
            if mid > 0 and tar > arr[mid-1]:
                return getClose(arr[mid], arr[mid-1], tar)
            end = mid-1
        else:
            if mid < n-1 and tar < arr[mid+1]:
                return getClose(arr[mid], arr[mid-1], tar)
            start = mid+1
    return arr[mid]


def getClose(val1, val2, tar):
    if tar-val1 >= tar-val2:
        return val2
    return val1


arr = [2, 5, 6, 7, 8, 8, 9]
n = len(arr)
target = 4
print(findClosest(arr, n, target))
