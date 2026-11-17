// LeetCode Solution: Make Sum Divisible By P
// Submitted: 2026-11-17T14:31:40.585Z
// Language: Python3

class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        r = sum(nums) % p

        if r == 0:
            return 0

        curr = 0
        best = n
        seen = {0:-1}

        for j, num in enumerate(nums):
            curr = (curr + num) % p 
            target = (curr - r + p) % p

            if target in seen:
                best = min(best, j-seen[target])
            seen[curr] = j
        
        return -1 if best == n else best