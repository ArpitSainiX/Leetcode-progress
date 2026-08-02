// LeetCode Solution: Count Subarrays With Even Odd Ratio I
// Submitted: 2026-08-02T08:12:35.639Z
// Language: Python3

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                x,y = 0,0
                subarr = nums[i:j+1]  #generated subarray
                for k in range(len(subarr)):
                    if subarr[k] % 2 == 0:
                        x += 1
                    else: 
                        y += 1
                if y > 0 and x*b <= y *a:
                    count += 1
        return count