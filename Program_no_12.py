from functools import reduce

lst = [1, 5, 2, 3, 6, 74, 98, 44, 72, 53, 1, 55, 13, 45, 4, 95, 8, 4, 6, 6, 6, 87, 54, ]
lst = list(map(lambda x: x + x, lst))
print(lst)

# lst = [1, 5, 2, 3, 6, 74, 98, 44, 53, 1, 55, 13, 45, 4, 95, 8, 4, 6, 6, 6, 87, 54, ]
lst = list(filter(lambda x: 0 if x % 2 == 0 else x, lst))
print(lst)

fact = lambda x: 1 if x == 0 else x * fact(x - 1)
print(fact(1))

n = int(input("enter No"))
print(reduce(lambda x, y: x * y, range(1, n + 1)))
