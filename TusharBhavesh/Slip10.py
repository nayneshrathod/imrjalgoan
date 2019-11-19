emoji={
    "Happy":"\U0001F62A",
    "Sleep":"\U0001F605"
}

msg=input("Enter the Message")
words=msg.split( )
outp=''

for item in words:
    if item in emoji:
        outp+=emoji.get(item)+ ' '
    else:
        outp+=item+' '

print(outp)