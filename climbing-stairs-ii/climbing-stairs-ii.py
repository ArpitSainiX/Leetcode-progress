// LeetCode Solution: Climbing Stairs Ii
// Submitted: 2026-11-10T17:51:29.428Z
// Language: Python3

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        f0, f1, f2 = 0,0,0

        for c in costs:
            f0, f1, f2 = f1, f2, min(f0+9, f1+4, f2+1)+c
        return f2












        # memo = {}

        # def helper(i):
        #     if i in memo:
        #         return memo[i]
        #     if i >= n:
        #         return 0
        #     min_cost = float('inf')
        #     for k in [1,2,3]:
        #         if i+k <= n:
        #             jump_penalty = k*k
        #             landing_cost = costs[i+k-1]
        #             min_cost = min(min_cost, landing_cost+jump_penalty + helper(i+k))
        #     memo[i] = min_cost
        #     return min_cost
        # return helper(0)