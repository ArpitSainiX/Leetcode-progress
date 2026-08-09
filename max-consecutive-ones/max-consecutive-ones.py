// LeetCode Solution: Max Consecutive Ones
// Submitted: 2026-08-09T09:26:45.493Z
// Language: Python3

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for el in nums:
            if el == 0:
                count = 0
            else:
                count += 1
            
            if res < count:
                res = count
        return res
            