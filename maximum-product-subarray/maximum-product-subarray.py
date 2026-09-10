// LeetCode Solution: Maximum Product Subarray
// Submitted: 2026-09-10T06:46:04.319Z
// Language: Python3

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #if the elements are more than 1.
        '''
            if elements multiplication is less than 0 then we need to remove element from the left side.
        '''
        multi = nums[0]
        curr_multi = 1

        for i in range(len(nums)):
            curr_multi *= nums[i]
            if curr_multi < 0:
                curr_multi //= multi
            elif curr_multi >= 0:
                multi = curr_multi
        
        return multi