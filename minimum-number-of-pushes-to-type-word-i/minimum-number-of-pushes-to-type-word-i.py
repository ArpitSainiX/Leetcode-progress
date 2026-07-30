// LeetCode Solution: Minimum Number Of Pushes To Type Word I
// Submitted: 2026-07-30T07:19:50.506Z
// Language: Python3

class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) < 8:
            return len(word)
        else:
            extra_letters = len(word)-8
            # return len(word) + extra_letters
            if len(word) % 2 == 0:
                return len(word)+ extra_letters
            else:
                return len(word)+ extra_letters+1