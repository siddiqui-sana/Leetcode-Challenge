# Write a function that prints Hello World 5 times!
# 1st Approach:
def hello():
    print("Hello World!")


hello()
hello()
hello()
hello()
hello()

# 2nd Approach:
def hello4():
    print("Hello World!")


def hello3():
    print("Hello World!")
    hello4()


def hello2():
    print("Hello World!")
    hello3()


def hello1():
    print("Hello World!")
    hello2()


def hello():
    print("Hello World!")
    hello1()


hello()
