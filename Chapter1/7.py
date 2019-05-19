"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column is set to 0.
"""


MATRIX = [[1, 0, 5], [2, 3, 4], [0, 6, 7]]
m = len(MATRIX)
n = len(MATRIX[0])


# Time Complexity = O(n)
# Space Complexity = O(n)
def set_row_col_zero_if_zero(matrix, m, n):
    rows_with_zero = []
    cols_with_zero = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows_with_zero.append(i)
                cols_with_zero.append(j)

    for row in rows_with_zero:
        for i in range(n):
            matrix[row][i] = 0

    for col in cols_with_zero:
        for j in range(m):
            matrix[j][col] = 0

    return matrix


print(set_row_col_zero_if_zero(MATRIX, m, n))
