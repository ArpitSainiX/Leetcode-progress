// LeetCode Solution: Binary Search
// Submitted: 2026-08-29T13:46:02.404Z
// Language: Python3

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return -1