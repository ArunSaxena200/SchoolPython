def set_matrix_zero(matrix):
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()

    # Identify rows and columns containing zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set entire rows to zero
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j] = 0

    # Set entire columns to zero
    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] = 0

    return matrix

# Example usage:
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

result = set_matrix_zero(matrix)
print(result)

101
000
101