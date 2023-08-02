def matrix_multiplication(matrix1, matrix2):
    """
    Multiply two matrices.

    Args:
        matrix1 (list of lists): First matrix.
        matrix2 (list of lists): Second matrix.

    Returns:
        list of lists: Resulting matrix after multiplication.
    """
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(element)
        result_matrix.append(row)
    
    return result_matrix

# Test the function
matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[7, 8], [9, 10], [11, 12]]
result_matrix = matrix_multiplication(matrix_a, matrix_b)

for row in result_matrix:
    print(row)
