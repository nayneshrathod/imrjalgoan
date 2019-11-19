# This File Is Genrated By A Naynesh Rathod
# Welcome to Naynesh Rathod PYTHON Prpgrams
'''
def reverse(s):
    return s[::-1]
def ispalindrom(s):
    rev=reverse(s)
    if(s==rev):
        return True
    return False
s=input("enter data")
ans=ispalindrom(s)
if ans==1:
    print("its palindrome")
else:
    print("its not plindrome")   '''
'''
 import os
path=input("enter path")
flst=[]
dlst=[]
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)):
        flst.append(i)
    else:
        dlst.append(i)
print(flst)
print(dlst)
n=int(input("enter no"))
temp=n
rev=0
while (n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("no is palin")

else:
        print("no is not palin")  
n = int(input("enter no"))
n1 = 0
n2 = 1
count = 2
if n > 0:
    print("fibbo sequence is")
    print(n1, ", ", n2, end=", ")
    while count < n:
        n3 = n1 + n2
        print(n3, end=', ')
        n1 = n2
        n2 = n3
        count += 1  
n=int(input("enter number"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if(n==sum):
    print("no is armstrong")
else:
        print("no is not armstrong")  
def my_function(x):
    return list(dict.fromkeys(x))
mylist=my_function(["abc","abc","rty"])
print(mylist) '''

name=[]
n=int(input("enter name"))
for i in range (n):
    print("enter name")
    name.append(input())
s=set(name)
name=list(s)
for x in name:
    print(x)


