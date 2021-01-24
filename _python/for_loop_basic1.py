# 1 Basic - Print all integers from 0 to 150.
count = 0
while count < 151:
    print(count)
    count += 1

# 2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000
count = 5
while count < 1001:
    print(count)
    count += 5

# 3 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for count in range(0, 101):
    if count % 10 == 0 :
        print("Coding Dojo")
    elif count % 5 == 0 :
        print("Coding")
    else:
        print(count)

# 4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
total = 0
for count in range(500001):
    if count % 2 == 0 :
        continue
    else : 
        total = total + count
print(total)

# 5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018, 0, -4) :
        print(x)

# 6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for y in range(lowNum, highNum + 1, 1) :
    if y % mult == 0 :
        print(y)
    else : 
        continue