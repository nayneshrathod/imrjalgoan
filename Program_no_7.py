import os

out = os.path.abspath("naynesh.txt")
print(out)

out = os.path.normpath("c:\\nasbas\sashbhb\\d//dasdas/d/ad/ada\\naynesh\\")
print(out)

out = os.path.split("c:\\nasbas\sashbhb\\d//dasdas/d/ad/ada\\naynesh\\")
print("Head  ", out[0])
print("tail ", out[1])
