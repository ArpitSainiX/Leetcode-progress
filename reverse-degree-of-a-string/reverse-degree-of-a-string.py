// LeetCode Solution: Reverse Degree Of A String
// Submitted: 2026-09-20T05:25:18.945Z
// Language: Python3

class Solution:
    def reverseDegree(self, s: str) -> int:
        mapped  = {
        "a":26, "b": 25, "c": 24, "d": 23, "e": 22, "f": 21, "g": 20, "h": 19, "i": 18, "j": 17, "k": 16, "l": 15, "m": 14, "n": 13, "o": 12, "p": 11, "q": 10,
        "r": 9, "s": 8, "t": 7, "u": 6, "v": 5, "w": 4, "x": 3, "y": 2, "z": 1
        }

        summ = 0 
        for i in range(len(s)):
            multi = 1
            if s[i] in mapped:
                multi *= (i+1) * mapped[s[i]]
                summ += multi
        return summ