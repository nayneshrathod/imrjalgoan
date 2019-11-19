lst = []
msg = input("enter A String ")
for i in msg.split():
    lst.append(i)
word = input("enetr remove word")
lst.remove(word)
msg = ""

for i in lst:
    msg += " " + i

print(msg)