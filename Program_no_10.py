m1 = int(input("enter 1s matrix rows"))
n1 = int(input("enter 1s matrix cols"))
a = [[0 for col in range(n1)] for row in range(m1)]
for i in range(m1):
    for j in range(n1):
        a[i][j] = int(input())

m2 = int(input("enter 2nd matrix rows"))
n2 = int(input("enter 2nd matrix cols"))
b = [[0 for col in range(n2)] for row in range(m2)]
for i in range(m2):
    for j in range(n2):
        b[i][j] = int(input())

c = [[0 for col in range(n2)] for row in range(m1)]
if n1 == m2:
    for i in range(m1):
        for j in range(n2):
            c[i][j] = 0
            for k in range(n1):
                c[i][j] += a[i][k] * b[k][j]
            print(c[i][j], end=' ')
        print("")
else:
    print("Mulitphication Not posible")

