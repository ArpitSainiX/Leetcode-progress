// LeetCode Solution: Two Sum
// Submitted: 2026-07-15T09:23:03.857Z
// Language: Python3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(1,n):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i,j]