// LeetCode Solution: Smallest Missing Multiple Of K
// Submitted: 2026-08-25T04:52:30.543Z
// Language: Python3

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()

        multiples = []*len(nums)

        for i in range(1, len(nums)+2):
            multi = k*i
            multiples.append(multi)
        
        for el in multiples:
            if el not in nums:
                return el

