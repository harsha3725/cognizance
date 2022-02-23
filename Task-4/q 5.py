def triangle(n):
    f = n - 1
    for d in range(0, n):
        for e in range(0, f):
            print(end=" ")
        f = f - 1
        for e in range(0, d + 1):
            print("* ", end="")
        print("\r")
n = 5
triangle(n)