import os
dirpath=input("Enter the Path")
os.chdir(dirpath)
print(os.listdir(dirpath))