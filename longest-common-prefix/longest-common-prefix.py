// LeetCode Solution: Longest Common Prefix
// Submitted: 2026-09-17T15:17:36.820Z
// Language: Python3

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()

        f,l = strs[0], strs[-1]
        ans = []
        for i in range(min(len(f), len(l))):
            if f[i] != l[i]:
                return "".join(ans)
            ans.append(f[i])
        
        return "".join(ans)