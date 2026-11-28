// LeetCode Solution: Longest Substring Without Repeating Characters
// Submitted: 2026-11-28T08:26:05.522Z
// Language: Python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            w = (r-l)+1
            length = max(length, w)
            seen.add(s[r])
        return length
                
            
