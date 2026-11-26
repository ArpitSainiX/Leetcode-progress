// LeetCode Solution: Stone Removal Game
// Submitted: 2026-11-26T08:07:02.854Z
// Language: Python3

class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        alice_turn = True

        while n >= remove:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn
        return not alice_turn