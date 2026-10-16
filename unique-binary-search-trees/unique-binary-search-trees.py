// LeetCode Solution: Unique Binary Search Trees
// Submitted: 2026-10-16T10:30:30.756Z
// Language: Python3

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        elif n > 2:
            return (n*(n-1)) - 1