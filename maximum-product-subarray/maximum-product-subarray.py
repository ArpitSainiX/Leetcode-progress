// LeetCode Solution: Maximum Product Subarray
// Submitted: 2026-09-10T07:10:12.432Z
// Language: Python3

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #if the elements are more than 1.
        '''
            first optimal approach.
        '''

        # n = len(nums)
        # pre = suff = 1
        # ans = float('-inf')

        # for i in range(len(nums)):
        #     if pre == 0:
        #         pre = 1
        #     if suff == 0:
        #         suff = 1 
            
        #     pre *= nums[i]
        #     suff *= nums[n-i-1]

        #     ans = max(ans, pre, suff)
        # return ans

        '''second optimal appraoch'''
        ans = maxProd = minProd = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            if curr < 0:
                maxProd, minProd = minProd, maxProd
            
            maxProd = max(curr, maxProd * curr)
            minProd = min(curr, minProd * curr)

            ans = max(ans, maxProd)
        return ans