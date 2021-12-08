def numRev(n):
    if n == 0:
        return
    numRev(n-1)
    print(n)
    
n = 5
numRev(5)