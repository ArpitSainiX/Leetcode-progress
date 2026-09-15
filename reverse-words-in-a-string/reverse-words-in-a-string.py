// LeetCode Solution: Reverse Words In A String
// Submitted: 2026-09-15T15:11:36.323Z
// Language: Python3

class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip() #first remove the whitespaces from the end and starting if any.

        sep = s.split()
        reverse = sep[::-1]
        return " ".join(reverse)