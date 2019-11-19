# Python Fibonacci series Program using While Loop

# Fibonacci series will start at 0 and travel upto below number
Number = int(input("\nPlease Enter the Range Number: "))

# Initializing First and Second Values of a Series
i = 0
First_Value = 0
Second_Value = 1

# Find & Displaying Fibonacci series
while (i < Number):
    if (i <= 1):
        Next = i
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = Next
    print(Next)
    i = i + 1


    # ? Remove Reptatd Elmet

n = int(input(
    "How many 'Elements' you want to store?"
))
lst = []
for item in range(n):
    lst.append(input())
print(lst)

lst = list(dict.fromkeys(lst))
print(lst)
