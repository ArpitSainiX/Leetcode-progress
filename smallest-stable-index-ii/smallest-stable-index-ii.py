// LeetCode Solution: Smallest Stable Index Ii
// Submitted: 2026-09-05T08:46:36.778Z
// Language: Python3

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffMin = []*n 
        prefMax = []*n


        for i in range(n):
            min_val = min(nums[i:n])
            max_val = max(nums[:i+1])
            suffMin.append(min_val)
            prefMax.append(max_val)

        res = []
        for j in range(n):
            subtract = prefMax[i] - suffMin[i]
            if subtract <= k:
                res.append(i) 
        
        if len(res) != 0:
            return min(res)
        return -1