import io

emoji = {
    "<3": "\U0001F221",
    "<3": "💋",
    ":D": "\U0001F305 ",
    ":A": "\U0001F325",
}

message = input("enter > ")
words = message.split(' ')
output = ''
for item in words:
    if item in emoji:
        output += emoji.get(item) + ' '
    else:
        output += item + ''
print(output)
'''
stud = {}
# while 1:
for i in range(3):
    sub = input("enter Key Name ")
    marks = int(input("enter Marks In Value "))
    while marks in stud.values():
        print("Duplicates Value ")
        marks = int(input("Enter Unique Value"))
    stud[sub] = marks
print(stud)
 fname = input("entr The Fol ANME ")
f = open(fname + ".txt", 'a')
s = input("Enter The Data")
f.writelines(s)
f.close()
 


def stars(j):
    for i in range(1, j, 2):
        print(' ' * j + i * '*')
        j -= 1

stars(int(input("entre no Of Stras")))
'''
