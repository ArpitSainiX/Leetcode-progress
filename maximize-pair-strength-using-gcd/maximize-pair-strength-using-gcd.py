// LeetCode Solution: Maximize Pair Strength Using Gcd
// Submitted: 2026-08-02T08:39:55.453Z
// Language: Python3

class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        maxStrength = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                strength = (nums[i]*nums[j]) // (math.gcd(nums[i], nums[j]) ** 2)
                maxStrength = max(maxStrength, strength)
        return maxStrength