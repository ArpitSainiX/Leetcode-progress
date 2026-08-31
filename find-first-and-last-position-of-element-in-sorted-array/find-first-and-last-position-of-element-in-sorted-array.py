// LeetCode Solution: Find First And Last Position Of Element In Sorted Array
// Submitted: 2026-08-31T06:36:29.170Z
// Language: Python3

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            l,r = 0, len(nums)-1
            result = -1

            while l <= r:
                mid = (l+r) //2
                if nums[mid] == target:
                    result = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return result
        
        def findLast(nums, target):
            l,r = 0, len(nums)-1
            result = -1

            while l <= r:
                mid = (l+r) //2
                if nums[mid] == target:
                    result = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return result

        first = findFirst(nums, target)
        if first == -1:
            return [-1, -1]
        last = findLast(nums, target)
        return [first, last]