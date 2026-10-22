// LeetCode Solution: Is Subsequence
// Submitted: 2026-10-22T15:54:45.551Z
// Language: Python3

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] not in t:
                return False
        return True