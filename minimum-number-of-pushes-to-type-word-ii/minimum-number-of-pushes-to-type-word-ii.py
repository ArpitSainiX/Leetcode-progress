// LeetCode Solution: Minimum Number Of Pushes To Type Word Ii
// Submitted: 2026-07-31T06:05:35.720Z
// Language: Python3

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for el in word:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1

        pushes = 0
        counts = sorted(freq.values(), reverse=True)

        for i, count in enumerate(counts):
            pushes += count * ((i//8)+1)
        return pushes