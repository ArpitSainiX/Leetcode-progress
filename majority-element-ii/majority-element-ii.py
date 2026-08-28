// LeetCode Solution: Majority Element Ii
// Submitted: 2026-08-28T04:35:38.416Z
// Language: Python3

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        appear = n // 3

        res = []
        freq = {}

        for el in nums:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1
        

        for k, v in freq.items():
            if v > appear:
                res.append(k)
        return res