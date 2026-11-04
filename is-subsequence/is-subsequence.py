// LeetCode Solution: Is Subsequence
// Submitted: 2026-11-04T16:59:14.180Z
// Language: Python3

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return False
        if len(t) == 0:
            return False
        p1, p2 = 0,0 
        count = 0

        while p1 < len(s) and p2 < len(t):
            if s[p1] != t[p2]:
                # p1 += 1
                p2 += 1
            elif s[p1] == t[p2]:
                count += 1
                p1 += 1
                p2 += 1
        
        if count == len(s):
            return True
        return False
