// LeetCode Solution: Find The Winning Player In Coin Game
// Submitted: 2026-08-19T09:06:55.885Z
// Language: Python3

class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        turns = min(x, y//4)
        if turns % 2 == 0:
            return "Bob"
        else:
            return "Alice"