import os

dir_path = input("Enter Path")
os.chdir(dir_path)
fname = input("Enter File NAme ")
try:
    f = open(fname, 'r')
    allcontaet = f.readlines()
    for item in allcontaet:
        print(item)
except IOError:
    print("File Doest Not Exits")
finally:
     # f.close()
    print("File Handling")
