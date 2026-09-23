// LeetCode Solution: Lucky Numbers In A Matrix
// Submitted: 2026-09-23T08:17:35.383Z
// Language: Python3

class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        min_arr = []
        max_arr = []
        for row in matrix:
            min_arr.append(min(row))
        

        for col in range(len(matrix[0])):
            max_num = max(matrix[row][col] for row in range(len(matrix)))
            max_arr.append(max_num)

        for el in min_arr:
            if el in max_arr:
                return [el]