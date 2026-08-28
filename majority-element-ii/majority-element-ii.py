// LeetCode Solution: Majority Element Ii
// Submitted: 2026-08-28T04:42:33.994Z
// Language: Python3

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = []

        for i in range(n):
            if len(res) == 0 or res[0] != nums[i]:
                cnt = 0
                for j in range(n):
                    if nums[j] == nums[i]:
                        cnt += 1
                if cnt > n//3:
                    res.append(nums[i])
            if len(res) == 2:
                break
        return res













        # n = len(nums)
        # appear = n // 3

        # res = []
        # freq = {}

        # for el in nums:
        #     if el in freq:
        #         freq[el] += 1
        #     else:
        #         freq[el] = 1
        

        # for k, v in freq.items():
        #     if v > appear:
        #         res.append(k)
        # return res