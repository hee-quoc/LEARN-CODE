# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
start = 2000
end = 3200

# Initialize an empty list to store the numbers
result = []

# Iterate through the range
for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 != 0:
        result.append(str(num))

# Join the list into a comma-separated string and print
print(", ".join(result))
