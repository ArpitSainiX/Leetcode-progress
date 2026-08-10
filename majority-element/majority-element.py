// LeetCode Solution: Majority Element
// Submitted: 2026-08-10T11:55:34.735Z
// Language: Python3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hs = {}
        for el in nums:
            if el in hs:
                hs[el] += 1
            else:
                hs[el] = 1

        for k, v in hs.items():
            if v > len(nums)//2:
                return k