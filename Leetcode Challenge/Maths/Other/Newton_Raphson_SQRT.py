def root(n):
    x = n
    while True:
        root = 0.5*(x+n/x)
        if abs(root-x) < 0.1:
            break
        x = root
    return root


n = 52
print(round(root(n), 3))
