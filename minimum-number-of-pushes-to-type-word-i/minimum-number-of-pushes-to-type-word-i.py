// LeetCode Solution: Minimum Number Of Pushes To Type Word I
// Submitted: 2026-07-30T07:16:14.359Z
// Language: Python3

class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) < 8:
            return len(word)
        else:
            extra_letters = len(word)-8
            return len(word) + extra_letters