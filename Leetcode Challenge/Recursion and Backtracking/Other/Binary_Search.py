def search(arr, target, start, end):
    if start > end:
        return -1
    mid = start+(end-start)//2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return search(arr, target, start, mid-1)
    return search(arr, target, mid+1, end)


arr = [1, 2, 3, 4, 55, 66, 78]
target = 55
print(search(arr, target, 0, len(arr)-1))