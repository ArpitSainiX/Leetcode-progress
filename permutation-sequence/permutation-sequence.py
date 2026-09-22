// LeetCode Solution: Permutation Sequence
// Submitted: 2026-09-22T06:10:33.138Z
// Language: Python3

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        strs = []
        for i in range(1, n+1):
            strs += str(i)
        
        ans = []
        def backtracking(curr):
            if len(curr) == len(strs):
                ans.append(curr.copy())
                return
            
            for num in strs:
                if num not in curr:
                    curr.append(num)
                    backtracking(curr)
                    curr.pop()
        backtracking([])
        return "".join(ans[k-1])