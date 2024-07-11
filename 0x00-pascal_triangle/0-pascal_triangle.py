def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    list: A list of lists, where each inner list represents a row of Pascal's Triangle.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's Triangle

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)  # Add the row to the triangle

    return triangle
