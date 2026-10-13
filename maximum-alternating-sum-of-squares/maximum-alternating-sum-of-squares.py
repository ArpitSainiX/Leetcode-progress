// LeetCode Solution: Maximum Alternating Sum Of Squares
// Submitted: 2026-10-13T16:12:24.483Z
// Language: Python3

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = sorted(i*i for i in nums)

        k = len(nums) // 2
        return sum(arr[k:]) - sum(arr[:k])