print("Arithmatic Operators Example")
a = 21
b = 10
c = 0

c = a + b
print("{} + {}  =   {}   ".format(a, b, c))

c = a - b
print("{} - {}  =   {}   ".format(a, b, c))

c = a * b
print("{} * {}  =   {}   ".format(a, b, c))

c = a / b
print("{} / {}  =   {}   ".format(a, b, c))

c = a % b
print("{} % {}  =   {}   ".format(a, b, c))

a = 2
b = 3
c = a ** b  # Exponent - Performs exponential (power) calculation on operators
print("{} ** {}  =   {}   ".format(a, b, c))

a = 10
b = 5
c = a // b  # Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed.
print("{} // {}  =   {}   ".format(a, b, c))

print("_" * 50)
print("Basic - Assignment Operators Example")
a = 21
b = 10
c = 0

c = a + b
print("Line 1 - Value of c is ", c)

c += a
print("Line 2 - Value of c is ", c)

c *= a
print("Line 3 - Value of c is ", c)

c /= a
print("Line 4 - Value of c is ", c)

c = 200
c %= a
print("Line 5 - Value of c is ", c)

c **= a
print("Line 6 - Value of c is ", c)

c //= a
print("Line 7 - Value of c is ", c)
print("_" * 50)
print("Bitwise Operators Example")
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0
c = a & b;  # 12 = 0000 1100
print("{} & {}  =   {}   ".format(a, b, c))

c = a | b;  # 61 = 0011 1101
print("{} | {}  =   {}   ".format(a, b, c))

c = a ^ b;  # 49 = 0011 0001
print("{} ^ {}  =   {}   ".format(a, b, c))

c = ~a;  # -61 = 1100 0011
print("~{}  =   {}   ".format(a, c))

c = a << 2;  # 240 = 1111 0000
print("{}  <<   2  =  {}".format(a, c))

c = a >> 2;  # 15 = 0000 1111
print("{}  >>   2  =  {} ".format(a, c))
print("_" * 52)
print("Basic - Comparison Operators")

a = 21
b = 10
c = 0

if (a == b):
    print("Line 1 - a is equal to b")
else:
    print("Line 1 - a is not equal to b")

if (a != b):
    print("Line 2 - a is not equal to b")
else:
    print("Line 2 - a is equal to b")

if b != a:
    print("Line 3 - a is not equal to b")
else:
    print("Line 3 - a is equal to b")

if (a < b):
    print("Line 4 - a is less than b")
else:
    print("Line 4 - a is not less than b")

if (a > b):
    print("Line 5 - a is greater than b")
else:
    print("Line 5 - a is not greater than b")

a = 5;
b = 20;
if (a <= b):
    print("Line 6 - a is either less than or equal to b")
else:
    print("Line 6 - a is neither less than nor equal to b")

if (b >= a):
    print("Line 7 - b is either greater than or equal to b")
else:
    print("Line 7 - b is neither greater than nor equal to b")

print("_" * 55)
print("Identity Operators ")

a = 20
b = 20

if (a is b):
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")

if (id(a) == id(b)):
    print("Line 2 - a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")

b = 30
if (a is b):
    print("Line 3 - a and b have same identity")
else:
    print("Line 3 - a and b do not have same identity")

if (a is not b):
    print("Line 4 - a and b do not have same identity")
else:
    print("Line 4 - a and b have same identity")

print("_" * 55)
print("Logical Operators ")
a = 10
b = 20
c = 0

if (a and b):
    print("Line 1 - a and b are true")
else:
    print("Line 1 - Either a is not true or b is not true")

if (a or b):
    print("Line 2 - Either a is true or b is true or both are true")
else:
    print("Line 2 - Neither a is true nor b is true")

a = 0
if (a and b):
    print("Line 3 - a and b are true")
else:
    print("Line 3 - Either a is not true or b is not true")

if (a or b):
    print("Line 4 - Either a is true or b is true or both are true")
else:
    print("Line 4 - Neither a is true nor b is true")

if not (a and b):
    print("Line 5 - a and b are true")
else:
    print("Line 5 - Either a is not true or b is not true")
print("_" * 50)
print("Membership Operators ")
a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")

if (b not in list):
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")

a = 2
if (a in list):
    print("Line 3 - a is available in the given list")
else:
    print("Line 3 - a is not available in the given list")