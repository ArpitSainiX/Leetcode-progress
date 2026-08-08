// LeetCode Solution: Move Zeroes
// Submitted: 2026-08-08T10:42:50.456Z
// Language: Python3

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r  = 0,1
        while l < r and r < len(nums):
            if nums[l] == 0 and nums[r] == 0:
                r += 1
            elif nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            elif nums[r] == 0:
                continue