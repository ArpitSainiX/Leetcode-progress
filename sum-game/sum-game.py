// LeetCode Solution: Sum Game
// Submitted: 2026-08-23T16:13:19.803Z
// Language: Python3

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        lsum = sum(int(c) for c in num[:half] if c != "?")
        rsum = sum(int(c) for c in numl[half:] if c != "?")


        lCount = num[:half].count("?")
        rCount = num[half:].count("?")

        return (lsum - rsum) != (rCount - lCount)*4.5