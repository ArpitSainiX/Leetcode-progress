// LeetCode Solution: Minimum Positive Sum Subarray
// Submitted: 2026-11-14T13:26:40.381Z
// Language: Python3

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # req_size = (r-l)+1
        ans = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                subarr = nums[i:j+1]

                if l <= len(subarr) <= r:
                    total = sum(subarr)

                    if total > 0:
                        ans.append(total)
                        
                



        if len(ans) == 0:
            return -1
        return min(ans)
