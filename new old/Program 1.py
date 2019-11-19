# arthemathic Operation
myint = 7
print(myint)

print(int(input("Enter First Num : ")) + int(input("Enter Second Num : ")))

print("Sum = ", int(input("Enter 1st number: ")) + int(input("Enter second number: ")))
myfloat = 7.1
print(myfloat)

myfloat = float(7)
print(myfloat)

vmstring = 'Hello'
print(vmstring)
vmstring = "Hello"
print(vmstring)

one = 1
two = 2
three = one + two
print(three)

h = 'Hello'
w = "World"
hw = h + " " + w
print(hw)

a, b, c = 1, 2, 3
print(a + b * c / three)
no1 = 22
no2 = 10
no3 = -15.21
print(no1 + no2)
print(no1 - no2)
print(no1 * no2)
print(no1 / no2)
print(no1 ** no2)
print(no1 // no2)
print(no2 + no3)
print(no2 - no3)
print(no3 // no2)

num = 5
for i in range(num):
    print("i = ", i)

string = "Naynesh Rathod"
for x in string:
    if x == ('e', 'a', 'o', 'i', 'u'):
        print(x.upper(), end=" ")
    else:
        print(x.lower(), end="")

list1 = ['physics', 'chemistry', 1997, 2000]

list2 = [1, 2, 3, 4, 5, 6, 7]
print("\n")
print("list1[0]: ", list1[0])
print("list1[-2]: ", list1[-2])
print("list1[1:]: ", list1[1:])
print("list2[1:5]: ", list2[1:5])

print("\n")
for i in range(2):
    print(i)
for i in range(4, 6):
    print(i)

print("\n")

counter = {}


def addToCounter(country):
    if country in counter:
        counter[country] += 1
    else:
        counter[country] = 1


addToCounter('China')
addToCounter('Japan')
addToCounter('china')
print(len(counter))

print("\n")

dictionary = {}
dictionary[1] = 1
print(dictionary)
dictionary['1'] = 6
print(dictionary)
dictionary[1] += 1
print(dictionary)
sum = 0
for k in dictionary:
    sum += dictionary[k]
print(sum)
