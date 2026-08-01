// LeetCode Solution: Number Of Good Pairs
// Submitted: 2026-08-01T07:48:43.190Z
// Language: Python3

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count
                    
