// LeetCode Solution: Count Numbers With Unique Digits
// Submitted: 2026-07-21T06:50:33.567Z
// Language: Python3

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        count = 0
        for i in range(10**n):
            if distinct(i):
                count += 1
        return count

        
def distinct(num):
    if num <= 10:
        return True
    s = str(num)
    hs = {}

    for i in range(0,len(s)):
        if int(s[i]) in hs:
            hs[int(s[i])] += 1
        else:
            hs[int(s[i])] = 1
    
    for k, v in hs.items():
        if v > 1:
            return False
    return True
