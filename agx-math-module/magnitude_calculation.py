import math

def vector_magnitude(vector):
    """
    Calculate the magnitude of a vector in 2D or 3D space.

    Args:
        vector (list): List representing the vector.

    Returns:
        float: Magnitude of the vector.
    """
    magnitude_squared = sum([component ** 2 for component in vector])
    magnitude = math.sqrt(magnitude_squared)
    return magnitude

# Test the function
vector_2d = [3, 4]
vector_3d = [1, 2, 2]

magnitude_2d = vector_magnitude(vector_2d)
magnitude_3d = vector_magnitude(vector_3d)

print("Magnitude (2D):", magnitude_2d)
print("Magnitude (3D):", magnitude_3d)
