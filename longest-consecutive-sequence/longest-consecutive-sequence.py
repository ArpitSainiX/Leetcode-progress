// LeetCode Solution: Longest Consecutive Sequence
// Submitted: 2026-09-11T09:36:44.541Z
// Language: Python3

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort() #then check the difference between the adjacent numbers, if it is 1 then increase the count by 1.
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        #if length of the nums > 1:
        maxLength = 1
        currLength = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue #skipping duplicates
            elif nums[i] == nums[i-1] + 1:
                currLength += 1
                maxLength = max(maxLength, currLength)
            else:
                currLength = 1
        
        return maxLength