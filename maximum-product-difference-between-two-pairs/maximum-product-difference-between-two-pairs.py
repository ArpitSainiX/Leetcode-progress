// LeetCode Solution: Maximum Product Difference Between Two Pairs
// Submitted: 2026-10-22T16:04:23.803Z
// Language: Python3

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        #nums = [7,6,5,4,2]

        return ((nums[0]*nums[1]) - (nums[-2]*nums[-1]))