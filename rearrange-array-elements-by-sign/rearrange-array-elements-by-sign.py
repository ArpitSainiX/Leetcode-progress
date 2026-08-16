// LeetCode Solution: Rearrange Array Elements By Sign
// Submitted: 2026-08-16T05:18:44.476Z
// Language: Python3

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg, res = [],[],[]

        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        
        res = [0]*(len(nums))
        res[0::2] = pos
        res[1::2] = neg
        return res

















        # pos, neg = [], []

        # for el in nums:
        #     if el > 0:
        #         pos.append(el) #Array of positive elements.
        #     else:
        #         neg.append(el) #Array of negaive elements.
        
        # res = []
        # l,r = 0,0

        # while l < len(pos) and r < len(neg):
        #     res.append(pos[l])
        #     res.append(neg[r])
        #     l += 1
        #     r += 1
        # return res
