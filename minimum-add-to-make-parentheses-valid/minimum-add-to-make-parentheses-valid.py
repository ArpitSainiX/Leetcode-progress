// LeetCode Solution: Minimum Add To Make Parentheses Valid
// Submitted: 2026-10-06T05:34:05.098Z
// Language: Python3

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l_arrow = s.count("(")
        r_arrow = s.count(")")

        if l_arrow == r_arrow:
            return 0
        
        abs_diff = abs(l_arrow - r_arrow)
        return abs_diff
