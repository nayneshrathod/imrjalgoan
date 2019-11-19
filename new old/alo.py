import random

name = 'Sample text'
char = random.choice(name)
print("random char is ", char)


# import random
import string

print("_"*60)

def randomString(stringLength):
    """Generate a random string of 5 charcters"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Random String is ", randomString(5) )

print("_"*60)


def mixString(s1, s2):
    resultString = s1[:1] + s2[:1] + s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(
        len(s2) / 2) + 1] + s1[len(s1) - 1] + s2[len(s2) - 1]
    print("Mix String is ", resultString)


s1 = "Naynesh"
s2 = "Rathod"
mixString(s1, s2)