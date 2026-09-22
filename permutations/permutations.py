// LeetCode Solution: Permutations
// Submitted: 2026-09-22T05:19:34.831Z
// Language: Python3

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def solve(vis, curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for i in range(len(nums)):
                if vis[i] == False:
                    curr.append(nums[i])
                    vis[i] = True
                    solve(vis, curr)
                    curr.pop()
                    vis[i] = False
        vis = [False]*n
        solve(vis, [])
        return ans







        # res = [] # it will store all the permutations.
        # path = []
        # used = [False]*len(nums)

        # def backtrack():
        #     if len(path) == len(nums):
        #         res.append(path[:])
        #         return
            
        #     for i in range(len(nums)):
        #         if used[i]:
        #             continue
                
        #         path.append(nums[i])
        #         used[i] = True
                
        #         backtrack()

        #         path.pop()
        #         used[i] = False
        # backtrack()
        # return res
