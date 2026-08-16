// LeetCode Solution: Rearrange Array Elements By Sign
// Submitted: 2026-08-16T05:15:09.405Z
// Language: Python3

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []

        for el in nums:
            if el > 0:
                pos.append(el) #Array of positive elements.
            else:
                neg.append(el) #Array of negaive elements.
        
        res = []
        l,r = 0,0

        while l < len(pos) and r < len(neg):
            res.append(pos[l])
            res.append(neg[r])
            l += 1
            r += 1
        return res
