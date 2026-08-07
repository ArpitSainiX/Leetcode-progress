// LeetCode Solution: Remove Duplicates From Sorted Array
// Submitted: 2026-08-07T04:34:27.548Z
// Language: Python3

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        for i in range(1,n):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1
