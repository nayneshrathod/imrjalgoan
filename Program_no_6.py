# This File Is Genrated By A Naynesh Rathod
# Welcome to Naynesh Rathod PYTHON Prpgrams

stud = [
    {'RollNo': '1', 'Name': 'Naynesh', 'classes': 'MCA'},
    {'RollNo': '2', 'Name': 'Ghanshyam', 'classes': 'MBM'},
    {'RollNo': '3', 'Name': 'Bhushan', 'classes': 'BCA'},
    {'RollNo': '4', 'Name': 'Paresh', 'classes': 'IMCA'},
]

print("This Is A Sample Print Oprtaion\n")
print("Sorted List by Roll No \n")
print(sorted(stud, key=lambda i: i['RollNo'], reverse=True), end="\n")
print("Sorted List by Name \n")
print(sorted(stud, key=lambda i: i['Name']))
print("Sorted List by Class\n")
print(sorted(stud, key=lambda i: i['classes']))
