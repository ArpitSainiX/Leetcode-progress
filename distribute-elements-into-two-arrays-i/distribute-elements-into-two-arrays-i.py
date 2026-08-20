// LeetCode Solution: Distribute Elements Into Two Arrays I
// Submitted: 2026-08-20T04:32:53.122Z
// Language: Python3

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [],[]

        for i in range(len(nums)):
            if i == 0:
                arr1.append(nums[i]) #appending first element to the array1.
            elif i == 1:
                arr2.append(nums[i]) #appending second element to the array2.
            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(nums[i])
                elif arr1[-1] < arr2[-1]:
                    arr2.append(nums[i])
        res = arr1 + arr2
        return res
