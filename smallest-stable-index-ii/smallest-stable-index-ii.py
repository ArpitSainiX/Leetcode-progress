// LeetCode Solution: Smallest Stable Index Ii
// Submitted: 2026-09-05T08:59:06.982Z
// Language: Python3

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suff = [0]*n 
        suff[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suff[i] = min(nums[i], suff[i+1])

        pre = float('-inf')
        for j in range(n):
            pre = max(pre, nums[j])

            if pre - suff[j] <= k:
                return j
        return -1