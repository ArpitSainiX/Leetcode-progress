// LeetCode Solution: Top K Frequent Elements
// Submitted: 2026-07-23T07:18:16.967Z
// Language: Python3

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        #bucket sort
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for num, v in count.items():
            freq[v].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


















        # nums.sort()
        # if len(nums) == 1:
        #     return nums
        # hs = {}

        # for el in nums:
        #     if el in hs:
        #         hs[el] += 1
        #     else:
        #         hs[el] = 1
        # res = []

        # for num in hs:
        #     res.append([hs[num], num])
        # res.sort(reverse=True)

        # final_ans = []
        # for i in range(k):
        #     final_ans.append(res[i][1])
        # return final_ans