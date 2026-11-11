// LeetCode Solution: Continuous Subarray Sum
// Submitted: 2026-11-11T16:10:05.234Z
// Language: Python3

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder = {0:-1}

        count = 0
        for i, el in enumerate(nums):
            count += el
            r = count % k

            if r not in remainder:
                remainder[count] = i
            elif i - remainder[r] > 1:
                return True
        return False