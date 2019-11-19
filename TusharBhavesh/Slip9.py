from functools import reduce

lst=[2,4,6,8,10]
lst=list(map(lambda x:x*x,lst))
print(lst)

lst=[78,10,15,20,70,75,40,33,21,98]
lst=list(filter(lambda x:x%5==0,lst))
print(lst)

lst=[6,7,8,2,4,9,1]
lst=reduce(lambda x,y:x+y,lst)
print(lst)

