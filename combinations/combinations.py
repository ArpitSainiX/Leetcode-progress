// LeetCode Solution: Combinations
// Submitted: 2026-09-22T08:27:04.600Z
// Language: Python3

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        curr = []

        def backtrack(st):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(st, n+1):
                curr.append(i)
                backtrack(i+1)
                curr.pop()
        backtrack(1)
        return res
        