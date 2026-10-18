// LeetCode Solution: Find All Numbers Disappeared In An Array
// Submitted: 2026-10-18T14:19:07.555Z
// Language: Python3

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        #search range is -> min(nums), len(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                res.append(i)
        return res