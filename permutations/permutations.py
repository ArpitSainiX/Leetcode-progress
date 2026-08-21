// LeetCode Solution: Permutations
// Submitted: 2026-08-21T15:19:14.268Z
// Language: Python3

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] # it will store all the permutations.
        path = []
        used = [False]*len(nums)

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
        return res
