// LeetCode Solution: Valid Palindrome
// Submitted: 2026-08-21T08:30:21.526Z
// Language: Python3

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in range(len(s)):
            if s[i].isalpha():
                new_str += s[i]
        lower = new_str.lower()


        l,r = 0,len(lower)-1
        while l < r:
            if lower[l] != lower[r]:
                return False
            else:
                l += 1
                r -= 1
        return True