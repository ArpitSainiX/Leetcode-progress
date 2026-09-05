// LeetCode Solution: Smallest Stable Index Ii
// Submitted: 2026-09-05T08:30:05.965Z
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