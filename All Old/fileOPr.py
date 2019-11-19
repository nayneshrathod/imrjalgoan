'''
def pattern(n):
    k = 2 * n - 2
    x = 65
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            ch = chr(x)
            print(ch, end=" ")
            x += 1
        print("\r")


pattern(8)

'''
'''
print("_" * 50)
for i in range(5):
    for j in range(5):
        # if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
        if j != 1 or j == 2 or i == 2 or j != 4:
            print("I", end="")
        else:
            print(end=" ")
    print()
'''

def swastika(row, col):
    for i in range(row):
        for j in range(col):
            if (i < row // 2):
                if (j < col // 2):
                    if (j == 0):
                        print("*", end="")
                    else:
                        print(" ", end=" ")
                elif (j == col // 2):
                    print(" *", end="")
                else:
                    if (i == 0):
                        print(" *", end="")

            elif (i == row // 2):
                print("* ", end="")
            else:
                if (j == col // 2 or j == col - 1):
                    print("* ", end="")
                elif (i == row - 1):
                    if (j <= col // 2 or j == col - 1):
                        print("* ", end="")
                    else:
                        print(" ", end=" ")
                else:
                    print(" ", end=" ")
        print()
swastika(7,7)
