// LeetCode Solution: Subarray Sum Equals K
// Submitted: 2026-08-17T10:02:52.431Z
// Language: Python3

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        currSum = 0
        count = 0
        for num in nums:
            currSum += num
            if (currSum - k) in freq:
                count += freq[currSum-k]
            if currSum in freq:
                freq[currSum] += 1
            else:
                freq[currSum] = 1
        return count
