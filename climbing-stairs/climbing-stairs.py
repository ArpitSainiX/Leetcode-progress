// LeetCode Solution: Climbing Stairs
// Submitted: 2026-11-23T15:58:43.767Z
// Language: Python3

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(i):
            if i == 1:
                return 1
            if i == 2:
                return 2
            return climb(i-1) + climb(i-2)
        return climb(n)