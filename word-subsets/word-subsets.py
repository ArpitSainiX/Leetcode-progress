// LeetCode Solution: Word Subsets
// Submitted: 2026-09-25T14:28:09.342Z
// Language: Python3

class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        freq = Counter()
        for word in words2:
            temp = Counter(word)
            for char in temp:
                freq[char] = max(freq[char], temp[char])
        
        res = []
        for word in words1:
            temp = Counter(word)
            if all(temp[char] >= freq[char] for char in freq):
                res.append(word)
        return res