// LeetCode Solution: Find Pivot Index
// Submitted: 2026-10-25T08:23:15.747Z
// Language: Python3

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)

        left = 0

        for i, x in enumerate(nums):
            if left == total - left - x:
                return i
            left += x
        return -1


        # n = len(nums)

        # prefix_sum = [0]*n
        # prefix_sum[0] = nums[0]

        # for i in range(1,n):
        #     prefix_sum[i] = prefix_sum[i-1] + nums[i]
        

        # total = prefix_sum[-1]
        # for i in range(len(prefix_sum)):
        #     left = prefix_sum[i-1] if i > 0 else 0 
        #     right = total - prefix_sum[i]
        #     if left == right:
        #         return i
        # return -1