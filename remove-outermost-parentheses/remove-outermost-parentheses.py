// LeetCode Solution: Remove Outermost Parentheses
// Submitted: 2026-10-08T15:58:07.659Z
// Language: Python3

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        level = 0

        for char in s:
            if char == "(":
                if level > 0:
                    res += char
                level += 1
            elif char == ")":
                level -= 1
                if level > 0:
                    res += char
        return res