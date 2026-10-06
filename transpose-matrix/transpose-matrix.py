// LeetCode Solution: Transpose Matrix
// Submitted: 2026-10-06T07:50:12.318Z
// Language: Python3

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of columns

        transpose = []
        for j in range(n):
            rows = []
            for i in range(m):
                rows.append(matrix[i][j])
            transpose.append(rows)
        return transpose 