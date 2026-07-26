// LeetCode Solution: Maximum Product Of Three Numbers
// Submitted: 2026-07-26T07:35:00.404Z
// Language: Python3

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        '''The product of three numbers will be max if and only if :
        it's the product of three largest positive numbers or
        it's the product of two negative numbers and one largest number.'''


        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])
