// LeetCode Solution: Smallest Missing Multiple Of K
// Submitted: 2026-08-25T04:51:38.599Z
// Language: Python3

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()

        multiples = []*(len(nums)+1)

        for i in range(1, len(nums)+1):
            multi = k*i
            multiples.append(multi)
        
        for el in multiples:
            if el not in nums:
                return el

