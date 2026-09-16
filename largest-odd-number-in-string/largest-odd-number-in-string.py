// LeetCode Solution: Largest Odd Number In String
// Submitted: 2026-09-16T15:30:09.268Z
// Language: Python3

class Solution:
    def largestOddNumber(self, s: str) -> str:
        i = 0
        while s[i] == "0":
            i += 1
        
        new_s = s[i: ] #example -> 32579
        r = len(new_s)-1 # pointing it to the last

        #currently i is at index 2
        while r >= i:
            if checkOdd(new_s[:r+1]):
                return new_s[:r+1]
            else:
                r -= 1 
        return ""



def checkOdd(string):
    num = int(string)
    if num % 2 != 0:
        return True