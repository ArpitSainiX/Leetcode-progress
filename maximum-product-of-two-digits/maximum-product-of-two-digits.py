// LeetCode Solution: Maximum Product Of Two Digits
// Submitted: 2026-07-25T06:36:44.134Z
// Language: Python3

class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)
        arr = [int(s[i]) for i in range(len(s))]
        
        arr.sort(reverse=True)
        final_s = ""
        for i in range(len(arr)):
            final_s += str(arr[i])
        
        fmax = int(final_s[0])
        smax = int(final_s[1])
        return fmax * smax