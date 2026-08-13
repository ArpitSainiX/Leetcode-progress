// LeetCode Solution: Maximum Subarray
// Submitted: 2026-08-13T15:55:15.780Z
// Language: Python3

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum = max(nums[i], nums[i]+curr_sum)
            maxSum = max(maxSum, curr_sum)
        return maxSum