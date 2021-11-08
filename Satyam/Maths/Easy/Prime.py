def isPrime(n):
    # 1st Approach:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

    # 2nd Approach:
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = 20
for i in range(2, n+1):
    print(str(i)+" --> "+str(isPrime(i)))
