// LeetCode Solution: Find All Numbers Disappeared In An Array
// Submitted: 2026-10-18T14:20:21.220Z
// Language: Python3

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        #search range is -> min(nums), len(nums)
        nums.sort()
        res = []
        for i in range(nums[0], len(nums)+1):
            if i not in nums:
                res.append(i)
        return res