// LeetCode Solution: Permutation Sequence
// Submitted: 2026-09-22T07:56:12.253Z
// Language: Python3

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        strs = [str(i) for i in range(1,n+1)]

        fact = [1]*n
        for i in range(1,n):
            fact[i] = fact[i-1]*i
        
        k -= 1
        ans = []

        for i in range(n, 0, -1):
            block = fact[i-1]
            idx = k // block
            k %= block
            ans.append(strs.pop(idx))
        return "".join(ans)




        # strs = []
        # for i in range(1, n+1):
        #     strs += str(i)
        
        # ans = []
        # def backtracking(curr):
        #     if len(curr) == len(strs):
        #         ans.append(curr.copy())
        #         return
            
        #     for num in strs:
        #         if num not in curr:
        #             curr.append(num)
        #             backtracking(curr)
        #             curr.pop()
        # backtracking([])
        # return "".join(ans[k-1])