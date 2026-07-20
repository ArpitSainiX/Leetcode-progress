// LeetCode Solution: Shift 2d Grid
// Submitted: 2026-07-20T07:22:13.615Z
// Language: Python3

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        total = m*n
        k = k % total

        res = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                #flattend index
                flat_i = r * n + c
                #new index after shifting
                new_flat_i = (flat_i + k) % total

                #convert 1D index back to 2D coordinates
                new_r = new_flat_i // n
                new_c = new_flat_i % n

                res[new_r][new_c] = grid[r][c]
        return res
