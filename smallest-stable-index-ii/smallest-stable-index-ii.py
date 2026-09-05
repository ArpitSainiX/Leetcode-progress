// LeetCode Solution: Smallest Stable Index Ii
// Submitted: 2026-09-05T08:49:37.053Z
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
            subtract = prefMax[j] - suffMin[j]
            if subtract <= k:
                res.append(j) 
        
        if len(res) != 0:
            return min(res)
        return -1