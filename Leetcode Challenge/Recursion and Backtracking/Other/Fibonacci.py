# Recursive program for the Fibonacci Series:
def fibo(n):
    # Base Condition
    if n < 2:
        return n
    # This is not a Tail Recursion!
    # Because, we are doing extra operations like Adding and Returing!
    return fibo(n-1)+fibo(n-2)

print(fibo(4))