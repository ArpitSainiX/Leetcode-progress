// LeetCode Solution: Subarray Sum Equals K
// Submitted: 2026-08-27T06:48:15.200Z
// Language: Python3

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # curr_sum = 0
        # count = 0

        # l,r = 0,1

        # while l <= r and r < len(nums):
        #     subarr = nums[l:r+1]
        #     curr_sum = sum(subarr)

        #     #checking conditions.
        #     if curr_sum > k:
        #         curr_sum -= nums[l]
        #         l += 1
        #     elif curr_sum < k:
        #         r += 1
        #     elif curr_sum == k:
        #         count += 1
        #         r += 1
        # return count

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
