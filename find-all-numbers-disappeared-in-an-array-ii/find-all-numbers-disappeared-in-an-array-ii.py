// LeetCode Solution: Find All Numbers Disappeared In An Array Ii
// Submitted: 2026-08-23T10:27:13.703Z
// Language: Python3

class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()

        res = []
        curr = lower

        for num in nums:
            if num < curr:
                continue
            
            if num > curr:
                res.append([curr, min(num-1, upper)])
            curr = num + 1

            if curr > upper:
                break
        if curr <= upper:
            res.append([curr, upper])
        return res
