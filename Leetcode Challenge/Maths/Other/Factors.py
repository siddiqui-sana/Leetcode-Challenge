# Time: O(n)
def fact1(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")

# Time: O(sqrt(n))
def fact2(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if n//i == i:
                print(i, end=" ")
            else:
                print(i, n//i, end=" ")

# Time and Space: O(sqrt(n))
def fact3(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if n//i == i:
                print(i, end=" ")
            else:
                print(i, end=" ")
                res.append(n//i)
    for j in range(len(res)-1, -1, -1):
        print(res[j], end=" ")


n = 20
fact1(n)
fact2(n)
fact3(n)
