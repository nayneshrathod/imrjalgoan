import os
dirpath=input("Enter the Path")
os.chdir(dirpath)
print(sorted(os.listdir(dirpath)))