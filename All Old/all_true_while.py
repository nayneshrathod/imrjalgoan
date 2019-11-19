'''
# This File Is Genrated By A Naynesh Rathod
# Welcome to Naynesh Rathod PYTHON Prpgrams
from builtins import int


def stars(n):
    for i in range(1, n + 1):
        print('* ' * i)


if __name__ == '__main__':
    while True:
        n = int(input("enter No"))
        if n==0:
            exit()
        else:
            stars(n)

import glob

import os

os.chdir('c:\\Users\\Naynesh\\PycharmProjects\\12-10-2019')
for i in glob.glob("*.py"):
    print("  " * 20, i)



my_str = input("enter the string")
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# Program to check if a string is palindrome or not
def DecimalToBinary(num):
    if num > 0:
        DecimalToBinary(num // 2)
        print(num % 2, end="")
        # print("       ", num % 2, end="")


DecimalToBinary(18)

print()


def decToBinary(n):
    # Size of an integer is
    # assumed to be 32 bits
    for i in range(31, -1, -1):
        k = n >> i
        if (k & 1):
            print("1", end="")
        else:
            print("0", end="")

            # Driver Code


n = 18
decToBinary(n)


def sumDigits(no):
    # if (no>0 and no<9):
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no // 10))
    # print(sum)


# Driver code
print(sumDigits(456))


list1 = []
n = int(input("Enter The Element Of Number"))
for i in range(0, n):
    el = int(input())
    list1.append(el)
print(list1)
plis = list(map(lambda x: x * 5, list1))
print("All List is a * 5 ", plis)
                      '''


def DecimalToBinary(num):
    if num > 0:
        DecimalToBinary(num // 2)
        print(num % 2, end="")


def DecimalToOctal(num):
    if num > 0:
        DecimalToOctal(num // 8)
        print(num % 8, end="")

def DecimalToHexa(num):
    if num > 0:
        DecimalToHexa(num // 16)
        print(num % 16, end="")

while True:
    ch = int(input(
        "Enter Yur choice\n" +
        "1 Decimal to Binary\n" +
        "2 Decimal to Octal\n" +
        "3 Decimal to HexaDecimal\n" +
        "0 For Exit"))
    if ch != 0:

        n = int(input("Enter To Check The Number"))
        if ch == 1:
            print("\n" * 2, "Decimal to Binary", DecimalToBinary(n))
        if ch == 2:
            print("\n" * 2, "Decimal to Octal", DecimalToOctal(n))
        if ch == 3:
            print("\n" * 2, "Decimal to HEXADecimal", DecimalToHexa(n))
    else:
        exit()
