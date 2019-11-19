'''
# Function for nth Fibonacci number

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:

        return Fibonacci(n - 1) + Fibonacci(n - 2)

    # Driver Program


print(Fibonacci(150))


'''

'''

FibonACI 
Fib = [0, 1]
for i in range(2, 700):
    Fib.append(Fib[i - 1] + Fib[i - 2])

print(Fib)
'''

'''
Using Def Function Fibonaci Number
def fb(n):
    Fib = [0, 1]
    n = n + 1
    for i in range(2, n):
        Fib.append(Fib[i - 1] + Fib[i - 2])
    # print(Fib)

    for h in Fib:
        print(h, end=", ")


fb(int(input("enter No")))

'''

# str() : Converting into string representation
odds = [1, 3, 67, 45, 83, 59]
year = 2017

print(odds)
print(str(odds) + " A list.\n")
print(year)
print(str(year) + " A year.\n")

fib_nums = [0, 1]

# just one line code
fib_nums = fib_nums + [fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2]) for i in range(2, 20)] * 0

# printing the series
print(fib_nums)

list[0]


tuple()