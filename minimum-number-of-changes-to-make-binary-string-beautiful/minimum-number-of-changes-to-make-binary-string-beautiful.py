// LeetCode Solution: Minimum Number Of Changes To Make Binary String Beautiful
// Submitted: 2026-11-18T16:00:31.031Z
// Language: Python3

class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(0, n-1, 2):
            if s[i+1] != s[i]:
                count += 1
        return count