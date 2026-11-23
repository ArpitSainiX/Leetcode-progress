// LeetCode Solution: Climbing Stairs
// Submitted: 2026-11-23T15:56:48.320Z
// Language: Python3

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return climb(n-1) + climb(n-2)
        return climb(n)