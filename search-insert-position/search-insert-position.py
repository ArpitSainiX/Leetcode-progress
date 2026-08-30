// LeetCode Solution: Search Insert Position
// Submitted: 2026-08-30T12:12:48.163Z
// Language: Python3

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            
        return l