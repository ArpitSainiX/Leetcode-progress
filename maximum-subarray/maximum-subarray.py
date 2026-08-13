// LeetCode Solution: Maximum Subarray
// Submitted: 2026-08-13T15:56:08.778Z
// Language: Python3

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curr_sum = nums[0]
        

        for i in range(1,len(nums)):
            curr_sum = max(nums[i], nums[i]+curr_sum)
            maxSum = max(maxSum, curr_sum)
        return maxSum