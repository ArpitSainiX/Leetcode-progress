// LeetCode Solution: Count Commas In Range
// Submitted: 2026-09-08T06:18:29.956Z
// Language: Python3

class Solution:
    def countCommas(self, n: int) -> int:
        if n < 999:
            return 0
        
        commas = 0
        if n >= 1000 and n < 100000:
            commas = (n - 1000) + 1
        elif n >= 100000:
            commas += 2*(n-100000)+1
        return commas