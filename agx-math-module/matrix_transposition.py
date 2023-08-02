def transpose_matrix(matrix):
    """
    Transpose a given matrix.

    Args:
        matrix (list of lists): The matrix to be transposed.

    Returns:
        list of lists: Transposed matrix.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

# Test the function
matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = transpose_matrix(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)
