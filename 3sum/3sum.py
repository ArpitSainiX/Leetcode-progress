// LeetCode Solution: 3sum
// Submitted: 2026-09-07T07:35:09.162Z
// Language: Python3

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() #sorting the array in ascending order.
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: #for removing duplicates and make them unique
                continue
            
            l,r = i+1, n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return ans