// LeetCode Solution: Find Target Indices After Sorting Array
// Submitted: 2026-10-19T14:39:03.569Z
// Language: Python3

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        
        return res