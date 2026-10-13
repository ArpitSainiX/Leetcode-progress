// LeetCode Solution: Maximum Alternating Sum Of Squares
// Submitted: 2026-10-13T16:10:48.777Z
// Language: Python3

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = [i*i for i in nums]

        k = len(nums) // 2
        ans = abs(sum(arr[k:]) - sum(arr[:k]))
        return ans