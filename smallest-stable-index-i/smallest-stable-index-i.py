// LeetCode Solution: Smallest Stable Index I
// Submitted: 2026-09-04T15:26:18.749Z
// Language: Python3

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = []
        for i in range(len(nums)):
            max_val = max(nums[:i+1])
            min_val = min(nums[i:n])

            instability = max_val - min_val
            if instability <= k:
                res.append(i)
        
        if len(res) != 0:
            return min(res)
        return -1
