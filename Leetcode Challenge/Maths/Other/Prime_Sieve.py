def seive(n, arr):
    for i in range(2, int(n**0.5)+1):
        if not arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = True
    for i in range(2, n+1):
        if not arr[i]:
            print(i, end=" ")


n = 40
arr = [False]*(n+1)
seive(n, arr)
