// LeetCode Solution: Single Element In A Sorted Array
// Submitted: 2026-09-06T08:23:13.187Z
// Language: Python3

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        freq = {}

        for el in nums:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1
        
        for k,v in freq.items():
            if v == 1:
                return k