def binarySqrt(n, p):
    start = 0
    end = n
    while start <= end:
        mid = start+(end-start)//2
        if mid*mid == n:
            return mid
        if mid*mid > n:
            end = mid-1
        else:
            start = mid+1
            root = mid
    incr = 0.1
    for _ in range(p):
        while root*root <= n:
            root += incr
        root -= incr
        incr /= 10
    return root


n = 40
p = 3
print(binarySqrt(n, p))