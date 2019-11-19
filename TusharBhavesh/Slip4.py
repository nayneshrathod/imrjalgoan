n=int(input(
    "How many 'Elements' you want to store?"
))
lst=[]
for item in range(n):
    lst.append(input())
print(lst)

lst=list(dict.fromkeys(lst))
print(lst)