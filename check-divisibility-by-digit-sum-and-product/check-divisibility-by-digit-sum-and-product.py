// LeetCode Solution: Check Divisibility By Digit Sum And Product
// Submitted: 2026-08-22T04:38:04.804Z
// Language: Python3

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if digitSumandMulti(n):
            return True
        return False

def digitSumandMulti(dig):
  s = str(dig)
  summ = 0
  multi = 1

  for i in range(len(s)):
    summ += int(s[i])
    multi *= int(s[i])
  
  totalSum = summ + multi
  if dig % totalSum == 0:
    return True
  return False