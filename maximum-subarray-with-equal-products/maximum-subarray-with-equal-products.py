// LeetCode Solution: Maximum Subarray With Equal Products
// Submitted: 2026-11-24T05:55:09.189Z
// Language: Python3

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        best = 0
    

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i:j+1]
                prod = math.gcd(*subarr) * math.lcm(*subarr)
                if prod == multi(subarr):
                    best = max(best, len(subarr))

        return best

def multi(arr):
    n = len(arr)
    mul = 1
    for el in arr:
        mul *= el
    return mul