// LeetCode Solution: Maximum Points You Can Obtain From Cards
// Submitted: 2026-10-27T11:47:11.131Z
// Language: Python3

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        curr = sum(cardPoints[:k])
        best = curr

        for i in range(1, k+1):
            curr += cardPoints[-i] - cardPoints[k-i]
            best = max(best, curr)
        return best
