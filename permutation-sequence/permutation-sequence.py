// LeetCode Solution: Permutation Sequence
// Submitted: 2026-09-22T05:58:02.994Z
// Language: Python3

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        strs = []
        for i in range(1, n+1):
            strs += str(i)

        
        ans = []
        def backtrack(idx):
            if idx == n:
                ans.append(strs.copy())
                return
            
            for i in range(idx, n):
                strs[i], strs[idx] = strs[idx], strs[i]
                backtrack(idx+1)
                strs[i], strs[idx] = strs[idx], strs[i]
        backtrack(0)

        return "".join(ans[k-1])
