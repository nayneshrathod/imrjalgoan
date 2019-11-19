stud={}
n=int(input("How man Records you want to store?"))
for item in range(n):
    sub=input("Enter the Key")
    marks=int(input("Enter the Values"))
    while marks in stud.values():
        print("Cant Added Duplicate Value")
        marks=int(input("Enter the Values"))
    stud[sub]=marks

print(stud)