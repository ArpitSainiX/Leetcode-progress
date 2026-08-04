// LeetCode Solution: Find Missing Elements
// Submitted: 2026-08-04T07:03:54.433Z
// Language: Python3

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(min(nums), max(nums)+1):
            if i not in nums:
                res.append(i)
        return res