// LeetCode Solution: Permutations Ii
// Submitted: 2026-08-22T04:52:23.852Z
// Language: Python3

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [] # it will store all the permutations.
        path = []
        used = [False]*len(nums)
        freq = []


        freq = []
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                path.append(nums[i])
                used[i] = True
                
                backtrack()

                path.pop()
                used[i] = False
        backtrack()
        for el in res:
            if el not in freq:
                freq.append(el)
        return freq
