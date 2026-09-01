// LeetCode Solution: Search In Rotated Sorted Array
// Submitted: 2026-09-01T08:35:34.861Z
// Language: Python3

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1