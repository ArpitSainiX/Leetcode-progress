// LeetCode Solution: Find Greatest Common Divisor Of Array
// Submitted: 2026-07-18T06:09:32.106Z
// Language: Python3

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        lnum = max(nums)
        snum = min(nums)

        return math.gcd(lnum, snum)