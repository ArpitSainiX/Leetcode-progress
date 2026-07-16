// LeetCode Solution: Find All Duplicates In An Array
// Submitted: 2026-07-16T07:47:37.574Z
// Language: Python3

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hs = {}

        for el in nums:
            if el in hs:
                hs[el] += 1
            else:
                hs[el] = 1
        
        ans = []
        for k,v in hs.items():
            if v > 1:
                ans.append(k)
        
        if len(ans) > 0:
            return ans
        else:
            return []