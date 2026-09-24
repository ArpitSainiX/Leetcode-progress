// LeetCode Solution: Smallest Index With Digit Sum Equal To Index
// Submitted: 2026-09-24T03:38:59.100Z
// Language: Python3

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # indices = []

        for i in range(len(nums)):
            string = str(nums[i])
            summ = 0
            for j in range(len(string)):
                summ += int(string[j])
            
            if summ == i:
                return i
        return -1
        
        # if len(indices) == 0:
        #     return -1
        # return min(indices)

