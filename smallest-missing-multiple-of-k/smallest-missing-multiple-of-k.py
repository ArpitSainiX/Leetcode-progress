// LeetCode Solution: Smallest Missing Multiple Of K
// Submitted: 2026-08-25T04:53:45.130Z
// Language: Python3

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set()
        i = 1
        while True:
            if i*k not in nums: return i*k
            else: i += 1
            




        # nums.sort()

        # multiples = []*len(nums)

        # for i in range(1, len(nums)+2):
        #     multi = k*i
        #     multiples.append(multi)
        
        # for el in multiples:
        #     if el not in nums:
        #         return el

