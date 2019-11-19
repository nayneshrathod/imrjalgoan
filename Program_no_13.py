from functools import reduce

lst = [1, 5, 2, 3, 6, 74, 98, 44, 72, 53, 1, 55, 13, 45, 4, 95, 8, 4, 6, 6, 6, 87, 54, ]
lst = list(map(lambda x: x + x, lst))
print(lst)

# lst = [1, 5, 2, 3, 6, 74, 98, 44, 53, 1, 55, 13, 45, 4, 95, 8, 4, 6, 6, 6, 87, 54, ]
lst = list(filter(lambda x: 0 if x % 3 == 0 else x, lst))
print(lst)

n = int(input("enter No for cheking a Factorial Number"))
print(reduce(lambda x, y: x * y, range(1, n + 1)), end="  ")

# This is A use For A Factorial lambda Funcation
fact = lambda x: 1 if x == 0 else x * fact(x - 1)
print(fact(8))
