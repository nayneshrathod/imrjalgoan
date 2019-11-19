# Function definition is here
def printinfo(name, age=35):
    "This prints a passed info into this function"
    print("Name: ", name, "Age ", age)
    return;


str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def nalayak():
    d = ""
    for i in str:

        d += i
        if i == " ":
            d += i
        print(d)


def changeme(mylist):
    "This changes a passed list into this function"
    mylist.append([1, 2, 3, 4])
    print("Values inside the function: ", mylist)
    return


mylist = [10, 20, 30];
changeme(mylist);
print("Values outside the function: ", mylist)

# Now you can call printinfo function
printinfo(age=25, name="Naynesh")
printinfo(name="Rathod")
nalayak()
