# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
start = 1000
end = 3000

result=[]

for i in range(start, end+1):
    if i % 2 == 0:
        result.append(str(i))

print(",".join(result))