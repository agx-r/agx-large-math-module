def add_vectors(vector1, vector2):
    """
    Add two vectors in 2D or 3D space.

    Args:
        vector1 (list): The first vector as a list of coordinates (x, y) or (x, y, z).
        vector2 (list): The second vector as a list of coordinates (x, y) or (x, y, z).

    Returns:
        list: The sum of the two vectors as a list of coordinates.
    """
    if len(vector1) == len(vector2):
        result_vector = [v1 + v2 for v1, v2 in zip(vector1, vector2)]
        return result_vector
    else:
        raise ValueError("Vectors must have the same number of dimensions (2D or 3D).")

# Test the function
vector_2d = [3, 5]
vector_3d = [1, 2, 4]
another_vector_2d = [2, -1]

sum_vector_2d = add_vectors(vector_2d, another_vector_2d)
sum_vector_3d = add_vectors(vector_3d, another_vector_2d)

print("Sum of 2D vectors:", sum_vector_2d)  # Output: [5, 4]
print("Sum of 3D vectors:", sum_vector_3d)  # Output: [3, 1, 3]
