// LeetCode Solution: Find All Numbers Disappeared In An Array
// Submitted: 2026-10-18T14:18:30.821Z
// Language: Python3

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        #search range is -> min(nums), len(nums)
        res = []
        for i in range(min(nums), len(nums)+1):
            if i not in nums:
                res.append(i)
        return res