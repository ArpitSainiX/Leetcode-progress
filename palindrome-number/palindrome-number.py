// LeetCode Solution: Palindrome Number
// Submitted: 2026-08-12T15:02:34.456Z
// Language: Python3

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_num = 0
        remain_num = x
        while remain_num > 0:
            digit = remain_num % 10
            reverse_num = (reverse_num * 10) + digit
            remain_num //= 10
        return (reverse_num == x)