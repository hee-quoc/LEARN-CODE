# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]


# Initialize the maximum variable to the smallest possible value
max_adjacent = float('-inf')

# Loop through the array to find the maximum value among adjacent pairs
for i in range(len(data3) - 1):
    max_adjacent = max(max_adjacent, max(data3[i], data3[i + 1]))

print(max_adjacent)
