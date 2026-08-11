// LeetCode Solution: Sort Colors
// Submitted: 2026-08-11T05:31:06.347Z
// Language: Python3

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n-i-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
