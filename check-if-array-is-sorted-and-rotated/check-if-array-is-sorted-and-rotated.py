// LeetCode Solution: Check If Array Is Sorted And Rotated
// Submitted: 2026-08-05T06:32:14.347Z
// Language: Python3

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%len(nums)]:
                count += 1
        return count <= 1