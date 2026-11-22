// LeetCode Solution: Check If All As Appears Before All Bs
// Submitted: 2026-11-22T14:48:43.770Z
// Language: Python3

class Solution:
    def checkString(self, s: str) -> bool:
        if "ba" in s:
            return False
        return True
        # res = []
        # ans = ""
        # for el in s:
        #     res.append(el)
        
        # res.sort()
        # ans = "".join(res)
        # return ans == s