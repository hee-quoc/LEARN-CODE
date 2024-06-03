# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

# Using nested loops to generate combinations
for i in data4:
    for j in data4:
        for k in data4:
            print(i, j, k)
