'''
import array

lis = [[2, 2], [5, 5]]
for i, x in enumerate(lis):
    for y in lis:
        print(lis[i] + lis[i], end=" ")
    print(end="\n ")
data = [66, 15, 91, 30, 35, 38, 43, 20, 38, 28, 98, 50, 7, 80, 99]

matrix1 = [[j for j in data]]
matrix2 = [[i for i in data[::-1]]]
print(matrix1 + matrix2)

filtered = [d for d in data if d > 50]
print(filtered)
matrix = [[1, 2], [3, 4], ]
flat = []
for j, row in enumerate(matrix):
    for i, num in enumerate(row):
        # print(row[i] * row[i])
        flat.append(row[j] * row[j])
print(flat)

# import  array
lis = []
n = int(input("enter the no  rows"))
m = int(input("enter the no  cols"))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        lis.append(int(input("enter nos")))
print(lis)

n = int(input("enter the no  rows"))
m = int(input("enter the no  cols"))

for i in range(1, n + 1):
    matrix2 = [[i for i in data[::-1]]]

for j in range(1, m + 1):
    matrix1 = [[j for j in data]]


print(matrix1 + matrix2)

n = 3
m = 3
val = [0] * n
for x in range (n):
    val[x] = [5] * m
print(val)

list1 = []
list2 = []

r = int(input("Enter Rows No"))
for i in range(1, r + 1):
    list1.append(int(input("enter no")))

c = int(input("Enter cols No"))
for i in range(1, c + 1):
    list2.append(int(input("enter no")))

result = map(lambda x, y: x + y, list1, list2)
print(list(result))
'''

X = [[8, 7, 3], [4, 5, 6], [7, 8, 9]]
Y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]

result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
for r in result:
    print(r)
