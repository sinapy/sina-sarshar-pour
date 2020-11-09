#Finidng the right Number
number = 44

x = number
# to find the answer we can use two methods, one mathematically and one with simple algorithm
#Finding the answer with algorithm

x1 = 1
x2 = 3

while x1 + x2 < x:
    x1 += 2
    x2 += 2

if x1 + x2 == x:
    print ("the two numbers are",x1,"and",x2)
else:
    print ("no solution exists")
