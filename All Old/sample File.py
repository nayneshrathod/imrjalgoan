fo = open("demo.txt", 'r')
s = fo.read()
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
fo.close()
print("Closed or not : ", fo.closed)

fo = open("demo.txt", 'a')
fo.write("\n#" + "_" * 55 + "\n" + s)
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)

fo.close()

fo = open("demo.txt", "wb")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
fo.close()


for x in range(1,10):
    print(x)