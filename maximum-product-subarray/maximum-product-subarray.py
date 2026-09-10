// LeetCode Solution: Maximum Product Subarray
// Submitted: 2026-09-10T07:00:00.400Z
// Language: Python3

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #if the elements are more than 1.
        '''
            if elements multiplication is less than 0 then we need to remove element from the left side.
        '''
        n = len(nums)
        pre = suff = 1
        ans = float('-inf')

        for i in range(len(nums)):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1 
            
            pre *= nums[i]
            suff *= nums[n-i-1]

            ans = max(ans, pre, suff)
        return ans