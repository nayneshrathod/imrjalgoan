import sqlite3
from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

Fullname = StringVar()
Email = StringVar()
gen = StringVar()
contry = StringVar()
chkjava = StringVar()
chkpython = StringVar()


def database():
    name1 = Fullname.get()  # abc
    email = Email.get()  # asas@gam.co
    gender = gen.get()  # male
    country = contry.get()  # india
    prog = chkjava.get() + chkpython.get()  # java
    conn = sqlite3.connect('registar.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Student (fn TEXT,em TEXT,gn TEXT  NOT NULL DEFAULT "MALE",cn TEXT,pr TEXT)')
    cursor.execute('INSERT INTO Student (fn,em,gn,cn,pr) VALUES(?,?,?,?,?)',
                   (name1, email, gender, country, prog,))
    conn.commit()


label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

Radiobutton(root, text="Male", padx=5, variable=gen, value="male").place(x=235, y=230)
Radiobutton(root, text="Female", padx=20, variable=gen, value="Female").place(x=290, y=230)

label_4 = Label(root, text="country", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

list1 = ['Canada', 'India', 'UK', 'Nepal', 'Iceland', 'South Africa'];

droplist = OptionMenu(root, contry, *list1)
droplist.config(width=15)
contry.set('select your country')
droplist.place(x=240, y=280)

label_4 = Label(root, text="Programming", width=20, font=("bold", 10))
label_4.place(x=85, y=330)
Checkbutton(root, text="java", variable=chkjava, onvalue="java ", offvalue="").place(x=235, y=330)

Checkbutton(root, text="python", variable=chkpython, onvalue="python ", offvalue="").place(x=290, y=330)

Button(root, text='Submit', width=20, fg='RED', command=database).place(x=180, y=380)

root.mainloop()
