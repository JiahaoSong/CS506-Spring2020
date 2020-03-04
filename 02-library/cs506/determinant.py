def isSquare(matrix):
    N = len(matrix)
    return all(len(row) == N for row in matrix)

def determinant(matrix):
    """
    Compute the determinant of a square matrix.

    Input: a 2D matrix

    Output: the determinant of the input
    """
    if matrix is None or len(matrix) == 0:
        raise ValueError("The matrix should not be empty.")

    if not isSquare(matrix):
        raise ValueError("The matrix must be square.")
    
    N = len(matrix) # the dimension of the matrix
    if N == 1:
        return matrix[0][0]
        
    result = 0
    for i in range(N):
        # ignore the 1st row and the i-th column
        subMatrix = [x[: i] + x[i + 1:] for x in matrix[1:]]
        result += ((-1) ** i) * matrix[0][i] * determinant(subMatrix)
    return result
