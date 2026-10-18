// LeetCode Solution: Find All Numbers Disappeared In An Array
// Submitted: 2026-10-18T14:28:23.495Z
// Language: Python3

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        #search range is -> min(nums), len(nums)
        seen = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in seen]
