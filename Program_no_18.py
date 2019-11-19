no = int(input("enter Ni"))
sum = 0
while no > 0 or sum > 9:
    if no == 0:
        no = sum
        sum = 0
    rem = no % 10
    sum += rem
    no //= 10
print("Addition of digit ", sum)


