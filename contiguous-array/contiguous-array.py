// LeetCode Solution: Contiguous Array
// Submitted: 2026-08-19T15:49:51.566Z
// Language: Python3

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        curr_sum = 0
        hs = {0:-1}

        for i, num in enumerate(nums):
            curr_sum += 1 if num == 0 else -1
            
            if curr_sum not in hs:
                hs[curr_sum] = i
            else:
                res = max(res, i - hs[curr_sum])
        return res
                 