// LeetCode Solution: Number Of Good Pairs
// Submitted: 2026-08-01T07:54:21.966Z
// Language: Python3

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if nums[i] == nums[j] and i < j:
        #             count += 1
        # return count
                    
        seen = {}
        count = 0
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        for i in seen:
            n = (seen[i]*(seen[i]-1))//2
            count += n
        return count