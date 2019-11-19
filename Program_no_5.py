a = [1, 2, 3]
try:
    print
    "Second element = %d" % (a[1])

    # Throws error since there are only 3 elements in array
    print
    "Fourth element = %d" % (a[3])

except IndexError:
    print
    "An error occurred"

try:
    a = 3
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

        # throws NameError if a >= 4
    print
    "Value of b = ", b

# note that braces () are necessary here for multiple exceptions
except(ZeroDivisionError, NameError):
    print
    "\nError Occurred and Handled"

# Program to depict Raising Exception

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print
    "An exception"
    raise  # To determine whether the exception was raised or not

try:
    f = open('missing')
    except OSError:
    print('It failed')
except FileNotFoundError:
    print('File not found')

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
