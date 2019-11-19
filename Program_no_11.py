def stras(n):
    for i in range(1, n, 2):
        print(" " * n + i * "*")
        n -= 1

stras(8)

