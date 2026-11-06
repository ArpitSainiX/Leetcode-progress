// LeetCode Solution: Reverse String
// Submitted: 2026-11-06T11:52:27.274Z
// Language: Python3

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1