# For each of the following code snippets, first predict the output(what you will see printed to the terminal). Once you've made a prediction, run the code snippet to see if you are correct!
# Score 11/15

#1
# Correct
# This will print 5 to the console
def a():
    return 5

print(a())


#2
# Correct
# This will print 10 to the console
def a():
    return 5

print(a()+a())

#3
# Wrong, this will return 5 and then the block will not execute anything after line 2. 
# This will print 5, 10 to the console
def a():
    return 5
    return 10

print(a())

#4
# Correct
# This will print 5 for the same reason as # 3 
def a():
    return 5
    print(10)

print(a())

#5
# Wrong, I knew this was a trap. It would have printed the 5 if the print() statement in a() had been a return statement. 
# This will print 5 to the console.
def a():
    print(5)

x = a()
print(x)

#6
# Wrong --- This printed line 1 - 3 line 2 - 5 line 3 - TypeError  I predicted line 3 but the function ran the print(b+c) for each time before the third line. I really need to think about each operation in order. 
# This will print none since the a function does not return a value.
def a(b, c):
    print(b+c)

print(a(1, 2) + a(2, 3))

#7
# Correct
# This will print 25 to the console. It might print because the return value is not stored to a variable. Nope, it prints.
def a(b, c):
    return str(b)+str(c)

print(a(2, 5))

#8
# Correct
# This will print line 1 - 100 line 2 - 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
	else:
		return 10
    return 7

print(a())

#9
# Correct
# This will print
# 7
# 14
# 21
def a(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3

print(a(2, 3))
print(a(5, 3))
print(a(2, 3) + a(5, 3))

#10
# Correct
# This will Print
# 8
def a(b, c):
    return b+c
    return 10

print(a(3, 5))

#11
# Wrong
# This will print
# 500
# 500
# 300
# 300 I got this line wrong. I forgot that the b with a() is not the universally defined b on line 1.
b = 500
print(b)
def a():
    b = 300
    print(b)

print(b)
a()
print(b)

#12
# Correct
# This will Print
# 500
# 500
# 300
# 300
# 500 
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b

print(b)
a()
print(b)

#13
# Correct
# This will print
# 500
# 500
# 300
# 300
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b

print(b)
b = a()
print(b)

#14
# Correct
# This will print
# 1
# syntax error, b() not defined
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)

a()

#15
# Correct
# This will print
# 1
# 3
# 5
# 10
def a():
    print(1)
    x = b()
    print(x)
    return 10

def b():
    print(3)
    return 5

y = a()
print(y)
