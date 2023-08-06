def dot_product(vector1, vector2):
    """
    Dot product of two vectors.

    Args:
        vector1 (list): List representing the first vector.
        vector2 (list): List representing the second vector.

    Returns:
        float: Dot product of the two vectors.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same dimension for dot product calculation.")
    
    result = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
    return result

# Test the function
vector_a = [2, 3, -1]
vector_b = [0, -1, 4]
dot_result = dot_product(vector_a, vector_b)

print("Dot Product:", dot_result)
