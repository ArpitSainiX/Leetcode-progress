// LeetCode Solution: Rotate Array
// Submitted: 2026-08-07T04:51:16.690Z
// Language: Python3

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.reverse() # nums = [7,6,5,4,3,2,1]
        k = k % n

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        

