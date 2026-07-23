// LeetCode Solution: Top K Frequent Elements
// Submitted: 2026-07-23T06:16:25.465Z
// Language: Python3

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        if len(nums) == 1:
            return nums
        hs = {}

        for el in nums:
            if el in hs:
                hs[el] += 1
            else:
                hs[el] = 1
        res = []

        for num in hs:
            res.append([hs[num], num])
        res.sort(reverse=True)

        final_ans = []
        for i in range(k):
            final_ans.append(res[i][1])
        return final_ans