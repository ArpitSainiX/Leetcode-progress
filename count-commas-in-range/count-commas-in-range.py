// LeetCode Solution: Count Commas In Range
// Submitted: 2026-09-08T06:22:55.185Z
// Language: Python3

class Solution:
    def countCommas(self, n: int) -> int:
        if n < 999:
            return 0
        
        commas = 0
        if n >= 1000:
            commas = n - 999
        return commas