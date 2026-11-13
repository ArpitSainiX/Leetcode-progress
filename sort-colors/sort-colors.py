// LeetCode Solution: Sort Colors
// Submitted: 2026-11-13T15:35:46.320Z
// Language: Python3

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l,r = 0, len(nums)-1
        i = 0 
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1


        # n = len(nums)
        # for i in range(n):
        #     for j in range(n-i-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
