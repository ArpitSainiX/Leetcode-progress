// LeetCode Solution: Check If All As Appears Before All Bs
// Submitted: 2026-11-22T14:48:00.928Z
// Language: Python3

class Solution:
    def checkString(self, s: str) -> bool:
        res = []
        ans = ""
        for el in s:
            res.append(el)
        
        res.sort()
        ans = "".join(res)
        return ans == s