def my_function(x):
    return list(dict.fromkeys(x))
mylist = my_function(["abc","cde","abc","ghi","pqr"])
print(mylist)


