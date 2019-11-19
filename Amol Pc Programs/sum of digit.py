n=int(input("Enter any number: "))
t=0
while(n>0):
    digit=n%10
    t=t+digit
    n=n//10
print("Sum of digit is: ",t)

