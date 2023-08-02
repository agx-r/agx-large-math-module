def cross_product(vector1, vector2):
    """
    Compute the cross product of two 3D vectors.

    Args:
        vector1 (list): List representing the first vector.
        vector2 (list): List representing the second vector.

    Returns:
        list: Resulting vector after cross product.
    """
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("Cross product is only defined for 3D vectors.")
    
    result_vector = [
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0]
    ]
    
    return result_vector

# Test the function
vector_1 = [2, 3, 4]
vector_2 = [5, 6, 7]
cross_product_result = cross_product(vector_1, vector_2)

print("Cross Product:", cross_product_result)
