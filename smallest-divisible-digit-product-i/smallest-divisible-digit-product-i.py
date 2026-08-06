// LeetCode Solution: Smallest Divisible Digit Product I
// Submitted: 2026-08-06T07:12:30.286Z
// Language: Python3

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 101):
            if digitProduct(i,t):
                return i



def digitProduct(a,t):
    s = str(a)
    multi = 1
    for i in range(len(s)):
        multi *= int(s[i])
    if multi % t == 0:
        return True
    
