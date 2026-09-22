// LeetCode Solution: Combinations
// Submitted: 2026-09-22T08:21:04.401Z
// Language: Python3

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        digits = [i for i in range(1,n+1)]
        ans = []
        def backtrack(curr):
            if len(curr) == k:
                ans.append(curr[:k])
                return
            
            for num in digits:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
            
        backtrack([])
        res = []

        for el in ans:
            el.sort()
            res.append(el)


        arr = []
        for num in res:
            if num in arr:
                continue
            arr.append(num)
        return arr