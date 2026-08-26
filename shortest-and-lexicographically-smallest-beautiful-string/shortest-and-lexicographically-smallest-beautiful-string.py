// LeetCode Solution: Shortest And Lexicographically Smallest Beautiful String
// Submitted: 2026-08-26T09:05:12.160Z
// Language: Python3

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        #edge case:
        if len(s) <= 2:
            return ""
        
        #where the actual algorithm will start.
        l,r = 0,2
        req_str = ""
        while l < r and r < len(s):
            subStr = s[l:r+1] #making the substr
            count = subStr.count("1") #counting 1's in subStr.
            
            if count < k:
                r += 1
            elif count > k:
                l += 1
            elif count == k:
                req_str = subStr
                l += 1
        return req_str