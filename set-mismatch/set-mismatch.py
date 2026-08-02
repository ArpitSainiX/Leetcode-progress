// LeetCode Solution: Set Mismatch
// Submitted: 2026-08-02T06:17:30.443Z
// Language: Python3

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        all_nums = [i for i in range(1,len(nums)+1)] #all_nums = [1,2,3,4]

        for el in all_nums:
            if el not in nums:
                res.append(el)
                break
        l,r = 0,1
        while l < r and r < len(nums):
            if nums[l] == nums[r]:
                res.append(nums[l])
                break
            else:
                l += 1
                r += 1
        return res

