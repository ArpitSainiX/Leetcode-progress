// LeetCode Solution: Set Matrix Zeroes
// Submitted: 2026-08-24T17:09:50.836Z
// Language: Python3

# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
        
#         n = len(matrix) #number of rows
#         m = len(matrix[0]) #number of columns

#         rows = set()
#         cols = set()

#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0:
#                     rows.add(i)
#                     cols.add(j)

#         for i in range(n):
#             for j in range(m):
#                 if i in rows or j in cols:
#                     matrix[i][j] = 0


class Solution:
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        # Step 1: Check if first row / first column originally have a zero
        for j in range(m):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        for i in range(n):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Step 2: Use first row & first column as markers for the rest of the matrix
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0   # mark row i
                    matrix[0][j] = 0   # mark column j

        # Step 3: Zero out cells based on markers (excluding first row/col for now)
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Zero out first row and first column if needed
        if first_row_has_zero:
            for j in range(m):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(n):
                matrix[i][0] = 0

        return matrix