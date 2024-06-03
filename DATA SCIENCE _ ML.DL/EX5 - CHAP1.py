#Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
def add_elements(matrix1, matrix2):
    # Ensure both matrices have the same number of rows
    if len(matrix1) != len(matrix2):
        raise ValueError("Both matrices must have the same number of rows")

    # Adding elements from matrix2 to matrix1 row by row
    result = []
    for row1, row2 in zip(matrix1, matrix2):
        result.append(row1 + row2)
    return result

# Given data
data5_list1 = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

# Adding elements
result = add_elements(data5_list1, data5_list2)

# Printing the result
for row in result:
    print(row)
