// LeetCode Solution: Product Of Array Except Self
// Submitted: 2026-07-24T06:25:58.848Z
// Language: Python3

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res