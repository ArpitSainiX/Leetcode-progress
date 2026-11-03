// LeetCode Solution: Minimum Moves To Equal Array Elements Iii
// Submitted: 2026-11-03T16:52:13.460Z
// Language: Python3

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx_num = max(nums)
        res = 0

        for el in nums:
            res += mx_num - el
        return res