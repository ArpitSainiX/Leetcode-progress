// LeetCode Solution: Determine Whether Matrix Can Be Obtained By Rotation
// Submitted: 2026-08-26T16:38:29.009Z
// Language: Python3

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            for i in range(n):
                for j in range(i+1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            for k in range(n):
                mat[k].reverse()
            
            if mat == target:
                return True
        return False