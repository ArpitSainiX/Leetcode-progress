// LeetCode Solution: Power Of Three
// Submitted: 2026-11-21T17:22:51.833Z
// Language: Python3

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(x):
            if x == 1:
                return True
            if x <= 0 or x % 3 != 0:
                return False
            return helper(x // 3)
        return helper(n)
    