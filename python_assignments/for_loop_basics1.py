#basic
for x in range(151):
    print(x)
#multiples of five
for x in range(0, 1001, 5):
    print(x)
#counting, the dojo way
for x in range(1, 101):
    if x % 5 == 0:
        print("Coding")
        continue
    elif x % 10 == 0:
        print("Coding Dojo")
        continue
    print(x)
#whoa. that sucker's huge
y=0
for x in range(0, 500001):
    if x % 2 != 0:
        y = y + x
    if x == 500000:
        print(y)
#countdown by fours
for x in range(2018, 0, -4):
    print(x)
#flexible counter
lowNum=1
highNum=1000
mult=4
for x in range(lowNum, highNum, 1):
    if x % mult == 0:
        print(x)