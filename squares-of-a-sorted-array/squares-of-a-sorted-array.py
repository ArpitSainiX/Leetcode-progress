// LeetCode Solution: Squares Of A Sorted Array
// Submitted: 2026-11-08T12:07:45.973Z
// Language: Python3

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # res = []
        # for el in nums:
        #     sq = el*el
        #     res.append(sq)
        # return sorted(res)


        for i in range(len(nums)):
            nums[i] = nums[i]**2
        return sorted(nums)