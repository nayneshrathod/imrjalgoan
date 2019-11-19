import random
print("In 20 And 30 Random Number Is:",+random.randrange(20,30))

x=['a','b','c','d','e']
print(random.choice(x))

random.shuffle(x)
print(x)

print(random.random())
