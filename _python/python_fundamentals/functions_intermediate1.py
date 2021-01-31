import random


def randInt(min=0, max=100):
    max2 = max - min
    num = random.random() * max2 + min
    num = round(num)
    return num


print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))

# Upon checking the solution I discovered that I did it correctly but did not combine the steps of code as I could have. Looking at it now I would rewrite the code as follows. 


def randInt(min=0, max=100):
    max_diff = max - min
    return round(random.random() * max_diff + min)


print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
