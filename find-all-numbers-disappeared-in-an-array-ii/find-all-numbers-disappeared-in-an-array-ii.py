// LeetCode Solution: Find All Numbers Disappeared In An Array Ii
// Submitted: 2026-08-23T10:22:52.152Z
// Language: Python3

class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()

        res = []
        elem = []

        for i in range(lower, upper+1):
            elem.append(i)
        
        l = 0 
        while l < len(elem):
            if elem[l] in nums:
                l += 1
                continue
            
            r = l
            while r < len(elem) and elem[r] not in nums:
                r += 1
            res.append([elem[l], elem[r-1]])
            l = r
        return res