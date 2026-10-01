// LeetCode Solution: Valid Parentheses
// Submitted: 2026-10-01T05:22:28.296Z
// Language: Python3

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')' : '(', ']' : '[', '}' : '{'}
        
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != pair[ch]:
                    return False
                stack.pop()
        return len(stack) == 0


