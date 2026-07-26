// LeetCode Solution: Maximum Product Of Three Numbers
// Submitted: 2026-07-26T07:30:58.963Z
// Language: Python3

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])
        