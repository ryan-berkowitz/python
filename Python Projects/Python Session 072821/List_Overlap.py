import random
a = random.sample(range(1, 100), random.randint(0,10))
print(a)
b = random.sample(range(1, 100), random.randint(0,10))
print(b)
c = list(set([x for x in a if x in b]))
print(c)