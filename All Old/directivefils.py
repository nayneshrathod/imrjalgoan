import os

dpath = os.path.dirname(os.path.realpath(__file__))
print("File Directory " + dpath)
with os.scandir('C:\\Users') as entries:
    for entry in entries:
        print(entry.name)

# list dir name and aothr feature
'''
out = os.listdir("C:\\Users\\Naynesh")
out1 = os.path.dirname("C:\\Users")
print("Directories Name", out1)
print("User Gives Directories files Sorted list   ")
for i in out:
   print(i)
'''

'''
while True:
   try:
       i = int(input("Enter First Number"))
       j = int(input("Enter Second Number"))
       print(i / j)
       exit()

   except ValueError:
       print("invalid Value")
   except ZeroDivisionError:
       print("Second Number CNNOT bE Zero")
   except IOError:
       print("IO ERROR Cannot Happen is this program")
   finally:
       print("GOod Bye IDIOT")
'''
