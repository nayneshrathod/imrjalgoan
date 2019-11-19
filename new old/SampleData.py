a, b = 0, 1
while a < 150:
    print(a, end="\t")
    a, b = b, a + b

print()
dcc = {'roll no': '46', 'name': "Swati Lohar", 'clas': 'MCA-III'}
d_cry = {'roll no': '26', 'name': "Naynesh Rathod", 'clas': 'MCA-I'}


print(dcc)
print(d_cry)


dict = {{'roll no': '36', 'name': "KHumesh Lohar", 'clas': 'MCA-II'},
        {'roll no': '36', 'name': "KHumesh Lohar", 'clas': 'MCA-II'}}

print(dict)


#  THis is Sample Data to working
#
# class Parent:  # define parent class
#     def myMethod(self):
#         print('Calling parent method')
#
#
# class Child(Parent):  # define child class
#     def myMethod(self):
#         # pass
#         print('Calling child method')
#
#
# c = Child()  # instance of child
# c.myMethod()  # child calls overridden method
#
# print()
#
#
# class Employee:
#     'Common base class for all employees'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name : ", self.name, ", Salary: ", self.salary)
#
#
# # print(Employee.__doc__())
# # "This would create first object of Employee class"
# emp1 = Employee("Zara", 2000)
# # "This would create second object of Employee class"
# emp2 = Employee("Manni", 5000)
#
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)
