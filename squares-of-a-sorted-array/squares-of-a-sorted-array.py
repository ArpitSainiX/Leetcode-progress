// LeetCode Solution: Squares Of A Sorted Array
// Submitted: 2026-11-08T12:06:25.821Z
// Language: Python3

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = []
        # nums = sorted(nums)
        for el in nums:
            sq = el*el
            res.append(sq)
        return sorted(res)