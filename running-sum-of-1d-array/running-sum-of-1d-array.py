// LeetCode Solution: Running Sum Of 1d Array
// Submitted: 2026-10-26T10:49:11.787Z
// Language: Python3

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix = [0]*len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        return prefix