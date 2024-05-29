# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
x=0
y=0
for i in data1:
    if i > 0:
        x+=1
    else:
        y+=1
print("Positive number:",x)
print("Negative number:",y)