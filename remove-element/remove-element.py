// LeetCode Solution: Remove Element
// Submitted: 2026-10-21T16:47:16.280Z
// Language: Python3

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k