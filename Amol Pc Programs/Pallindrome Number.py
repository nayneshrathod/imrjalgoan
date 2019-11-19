n = int(input("Enter any number: "))
temp = n
rev = 0
while (n > 0):
    k = n % 10
    rev = rev * 10 + k

    n = n // 10
if (temp == rev):
    print("The number is a pallindrome")
else:
    print("The number is not a pallindrome")
