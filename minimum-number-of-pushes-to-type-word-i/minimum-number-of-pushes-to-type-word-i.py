// LeetCode Solution: Minimum Number Of Pushes To Type Word I
// Submitted: 2026-07-30T07:23:49.618Z
// Language: Python3

class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        for i in range(len(word)):
            pushes += (i//8) + 1
        return pushes