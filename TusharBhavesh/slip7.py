lst=[]

def DecimalToBin(num):
    if num>0:
        lst.append(num%2)
        DecimalToBin(num//2)
    print(lst[::-1])

def DecimaltoOct(num):
    if num>0:
        lst.append(num%8)
        DecimaltoOct(num//8)
    print(lst[::-1])

def DecimaltoHex(num):
    if num>0:
        lst.append(num%16)
        DecimaltoHex(num//16)
    print(lst[::-1])

while 1:
    n=int(input("\nEnter the Number"))
    ch=int(input("Enter 1.Binary\n2.For Octal\n3For HexaDecimal\n4Exit"))

    if ch <= 3:
        if ch == 1:
            DecimalToBin(n)

        if ch == 2:
            DecimaltoOct(n)

        if ch == 3:
            DecimaltoHex(n)

    if ch == 4:
        break

print(oct(17))


