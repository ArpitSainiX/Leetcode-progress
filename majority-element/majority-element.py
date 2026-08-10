// LeetCode Solution: Majority Element
// Submitted: 2026-08-10T11:56:09.311Z
// Language: Python3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
        # hs = {}
        # for el in nums:
        #     if el in hs:
        #         hs[el] += 1
        #     else:
        #         hs[el] = 1

        # for k, v in hs.items():
        #     if v > len(nums)//2:
        #         return k