# Write a function that takes a number and print the series till 5!
# Let's say  1 2 3 4 5
def numbers(n):
    if n == 5:
        print(n)
        return
    print(n)
    # This is called Tail Recursion!
    # This is the last function call!
    numbers(n+1)
numbers(1)
