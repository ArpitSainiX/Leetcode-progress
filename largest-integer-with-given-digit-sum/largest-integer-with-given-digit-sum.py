// LeetCode Solution: Largest Integer With Given Digit Sum
// Submitted: 2026-07-26T07:42:55.462Z
// Language: Python3

class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0
        
        largest = -1
        for i in range(1,10**n):
            if digitSum(i,s):
                largest = i
            
        return largest



    

def digitSum(num,s):
    str_num = str(num)
    summ = 0
    for i in range(len(str_num)):
        summ += int(str_num[i])
    if summ == s:
        return True
    return False