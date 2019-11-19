n = int(input())


def arm(n1):
    for n in range(1, n1 + 1):
        cot = len(str(n))
        sum, temp = 0, n
        while temp > 0:
            dig = temp % 10
            sum += dig ** cot
            temp //= 10
        if sum == n:
            print(n, end=" ")


arm(n)
