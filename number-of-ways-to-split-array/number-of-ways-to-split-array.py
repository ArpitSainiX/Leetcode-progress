// LeetCode Solution: Number Of Ways To Split Array
// Submitted: 2026-10-28T15:39:00.960Z
// Language: Python3

class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_arr = [0]*len(nums)
        prefix_arr[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_arr[i] = prefix_arr[i-1] + nums[i]
        
        total = prefix_arr[-1]
        count = 0
        for i in range(len(prefix_arr)-1):
            if prefix_arr[i] >= total - prefix_arr[i]:
                count += 1
        return count