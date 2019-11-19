Student=[{'RollNo':1,'Name':'Tushar','Class':'MCA'},
         {'RollNo':2,'Name':'Bhavesh','Class':'IMCA'},
         {'RollNo':3,'Name':'Nano','Class':'HMCA'}]

print(Student)
print(sorted(Student,key=lambda i:i['Name']))
print(sorted(Student,key=lambda i:i['Class']))
print(sorted(Student,key=lambda i:i['RollNo'],reverse=True))