// LeetCode Solution: Climbing Stairs
// Submitted: 2026-11-23T16:01:18.195Z
// Language: Python3

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one






        # def climb(i):
        #     if i == 1:
        #         return 1
        #     if i == 2:
        #         return 2
        #     return climb(i-1) + climb(i-2)
        # return climb(n)