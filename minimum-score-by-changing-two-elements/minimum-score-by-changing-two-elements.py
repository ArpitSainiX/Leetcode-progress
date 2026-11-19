// LeetCode Solution: Minimum Score By Changing Two Elements
// Submitted: 2026-11-19T16:07:56.768Z
// Language: Python3

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()

        return min(nums[-1] - nums[2],
            nums[-2] - nums[1],
            nums[-3] - nums[0]
        ) 