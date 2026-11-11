// LeetCode Solution: Continuous Subarray Sum
// Submitted: 2026-11-11T16:11:43.553Z
// Language: Python3

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder = {0:-1}

        total = 0
        for i, el in enumerate(nums):
            total += el
            r = total % k

            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False