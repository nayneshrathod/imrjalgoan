def prime(no):
    for val in range(2, no + 1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                print(val, end=" ")


def armstrong(num):
    for num in range(1, num + 1):
        # order of number
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            print(num, end=" ")


# print(armstrong(int(input("enter No"))))
# function to check string is
# palindrome or not
def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, len(str) / 2):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")
