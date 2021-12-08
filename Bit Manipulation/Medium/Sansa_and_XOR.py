def sansaXor(arr):
    n = len(arr)
    res = 0
    if n % 2 == 0:
        return 0
    for i in range(0, n, 2):
        res ^= arr[i]
    return res
