import os

file_name = input("enter File name ")
file = file_name + ".py"
path = input("enter Path  ")
os.chdir(path)
fcnt = 0
try:
    f = open(file, 'r')
    f1 = f.readlines()
    print("No of Lines ", len(f1))
    for i in f1:
        cnt = i.split()
        fcnt += len(cnt)
        print(i)

    print("Total Word ", fcnt)
except IOError:
    print("Does Not Exist")
finally:
    # f.close()
    print("File Handling")
