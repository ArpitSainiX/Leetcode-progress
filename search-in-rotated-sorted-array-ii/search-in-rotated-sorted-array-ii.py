// LeetCode Solution: Search In Rotated Sorted Array Ii
// Submitted: 2026-09-06T08:16:49.316Z
// Language: Python3

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # if target in nums:
        #     return True
        # return False

        l,r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            #if mid is the target.
            if nums[mid] == target:
                return True

            #if no sorted part found.
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
            
            #checking if the left part is sorted or not.
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            #checking if the right part is sorted or not.
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else: 
                    r = mid - 1
        return False


            
