def subtract_vectors(vector1, vector2):
    """
    Subtract one vector from another in 2D or 3D space.

    Args:
        vector1 (list): List representing the first vector.
        vector2 (list): List representing the second vector.

    Returns:
        list: Resulting vector after subtraction.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same dimension for subtraction.")
    
    result_vector = [v1 - v2 for v1, v2 in zip(vector1, vector2)]
    return result_vector

# Test the function
vector_2d = [3, 7]
vector_3d = [1, 4, 2]
another_vector_2d = [0, -2]
another_vector_3d = [2, -2, 0]
result_2d = subtract_vectors(vector_2d, another_vector_2d)
result_3d = subtract_vectors(vector_3d, another_vector_3d)

print("Result (2D):", result_2d)
print("Result (3D):", result_3d)
