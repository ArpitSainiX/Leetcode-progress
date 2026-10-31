// LeetCode Solution: Count Number Of Nice Subarrays
// Submitted: 2026-10-31T14:27:48.126Z
// Language: Python3

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        prefixSum = 0
        freq = [0]*(len(nums)+1)
        freq[0] = 1
        count = 0

        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum >= k:
                count += freq[prefixSum-k]
            freq[prefixSum] += 1
        return count