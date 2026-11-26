// LeetCode Solution: Stone Removal Game
// Submitted: 2026-11-26T08:11:32.496Z
// Language: Python3

class Solution:
    def canAliceWin(self, n: int) -> bool:
        # remove = 10
        # alice_turn = True

        # while n >= remove:
        #     n -= remove
        #     remove -= 1
        #     alice_turn = not alice_turn
        # return not alice_turn

        remove, moves = 10,0

        while n >= remove:
            n -= remove
            remove -= 1
            moves += 1
        return moves % 2 == 1