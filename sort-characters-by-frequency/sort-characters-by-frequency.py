// LeetCode Solution: Sort Characters By Frequency
// Submitted: 2026-08-01T15:51:30.111Z
// Language: Python3

class Solution:
    def frequencySort(self, s: str) -> str:
        hs = {}
        for i in s:
            if i in hs:
                hs[i] += 1
            else:
                hs[i] = 1
        
        #hs = {"t":1, "r":1, "e":2}
        descend_order = dict(sorted(hs.items(), key=lambda item:item[1], reverse=True))
        res = ""

        for k,v in descend_order.items():
            res += k*v
        return res
