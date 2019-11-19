


print("Print Student Details Withs Its Full Details\n")
stud_name = input("Enter The Student  name ")
python = int(input("Enter Python Marks"))
Adnroid = int(input("Enter Adnroid Marks"))
NLP = int(input("Enter NLP Marks"))
Drupal = int(input("Enter Drupal Marks"))
Compiler_C = int(input("Enter Compiler_C Marks"))
total = python + Adnroid + NLP + Drupal + Compiler_C
Avra = total / 5
per = (total / 500) * 100
print("Name : ", stud_name)
print("Total Marks : ", total)
print("Marks Percentage :  ", float(per))
print("Marks Avarage  : ", Avra)
if per > 90 and 100 >= per:
    print("Grade is  O")
if per > 75 and 90 >= per:
    print("Grade is  A+")
if per > 65 and 75 >= per:
    print("Grade is  B")
if per > 50 and 65 >= per:
    print("Grade is  B+")
if per > 40 and 50 >= per:
    print("Grade is  C")
if per <= 40:
    print("Fail")
