// LeetCode Solution: Third Maximum Number
// Submitted: 2026-07-17T07:28:40.001Z
// Language: Python3

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        set01 = set(nums)
        arr = list(set01)
        arr.sort(reverse=True)
        if len(arr) < 3:
            return max(arr)
        else:
            return arr[2]
