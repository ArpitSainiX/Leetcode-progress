// LeetCode Solution: Jump Game
// Submitted: 2026-07-22T05:09:13.247Z
// Language: Python3

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        far = 0

        for i in range(n):
            if i > far:
                return False
            far = max(far, i + nums[i])
            if far >= n-1:
                return True
        return True