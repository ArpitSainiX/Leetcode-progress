// LeetCode Solution: Maximum Product Of Two Elements In An Array
// Submitted: 2026-07-27T05:46:16.714Z
// Language: Python3

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        ans = (nums[-1]-1) * (nums[-2]-1)
        return ans