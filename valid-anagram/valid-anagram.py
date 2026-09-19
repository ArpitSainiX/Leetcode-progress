// LeetCode Solution: Valid Anagram
// Submitted: 2026-09-19T12:53:43.384Z
// Language: Python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        s2 = sorted(t)

        if s1 == s2:
            return True
        return False