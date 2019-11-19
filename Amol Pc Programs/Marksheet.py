CPP=int(input("Enter The First Subject Marks"))
DS=int(input("Enter The Second Subject Marks"))
Java=int(input("Enter The Third Subject Marks"))
NLP=int(input("Enter The Fourth Subject Marks"))
Python=int(input("Enter The Fifth Subject Marks"))

print("C++ Marks Is",+CPP)
print("Data Struct Marks Is",+DS)
print("Java Marks Is",+Java)
print("NLP Marks Is",+NLP)
print("Python Marks Is",+Python)

per=(CPP+DS+Java+NLP+Python)/5
print("percentage",+per,"%")
if per>=85:
    print("Grade :A+")
elif per>=70:
    print("Grade :A")
elif per>=65:
    print("Grade :B")