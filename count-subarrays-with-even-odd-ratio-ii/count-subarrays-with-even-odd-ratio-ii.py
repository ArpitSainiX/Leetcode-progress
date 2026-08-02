// LeetCode Solution: Count Subarrays With Even Odd Ratio Ii
// Submitted: 2026-08-02T08:18:33.747Z
// Language: Python3

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        count = 0
        for i in range(len(nums)):
            x,y = 0,0
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    x += 1
                else:
                    y += 1
                if y > 0 and x*b <= y *a:
                    count += 1
        return count