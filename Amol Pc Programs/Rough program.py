n=int(input("How many element you want to read "))
lst=[]
for i in range(n):
    lst.append(input())
print(lst)

lst=list(dict.fromkeys(lst))
print(lst)