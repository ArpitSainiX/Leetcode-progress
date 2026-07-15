// LeetCode Solution: Gcd Of Odd And Even Sums
// Submitted: 2026-07-15T09:26:04.506Z
// Language: Python3

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        evenSum = 0
        oddSum = 0

        for i in range(1, 2*n+1):
            if i % 2 == 0:
                evenSum += i
            else:
                oddSum += i
        return math.gcd(evenSum, oddSum)