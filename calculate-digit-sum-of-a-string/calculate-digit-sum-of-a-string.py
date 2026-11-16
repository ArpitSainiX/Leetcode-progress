// LeetCode Solution: Calculate Digit Sum Of A String
// Submitted: 2026-11-16T16:15:42.836Z
// Language: Python3

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            string = []

            for i in range(0, len(s), k):
                string.append(str(sum(int(c) for c in s[i:i+k])))
            s = "".join(string)
        return s