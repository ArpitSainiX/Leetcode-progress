// LeetCode Solution: Shortest And Lexicographically Smallest Beautiful String
// Submitted: 2026-08-26T09:16:45.574Z
// Language: Python3

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""

        ans = ""
        l = 0
        ones = 0

        for r in range(len(s)):
            if s[r] == "1":
                ones += 1
            while ones == k:
                
                while s[l] == "0":
                    l += 1

                subStr = s[l : r + 1]

                if not ans or len(subStr) < len(ans) or (len(subStr) == len(ans) and subStr < ans):
                    ans = subStr
                if s[l] == "1":
                    ones -= 1
                l += 1

        return ans