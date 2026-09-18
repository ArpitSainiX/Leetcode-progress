// LeetCode Solution: Rotate String
// Submitted: 2026-09-18T16:19:28.529Z
// Language: Python3

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #if s is already equal to goal.
        if len(s) != len(goal):
            return False
        if s == goal:
            return True

        #if they are not already equal
        for i in range(len(s)):
            f = s[0]
            s = s[1:]
            s += f

            if s == goal:
                return True
        return False