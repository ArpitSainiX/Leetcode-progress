// LeetCode Solution: Count Days Spent Together
// Submitted: 2026-10-24T11:27:05.703Z
// Language: Python3

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_day_number(date):
            month = int(date[:2])
            day = int(date[3:])
            return sum(days[:month - 1]) + day

        start = max(to_day_number(arriveAlice), to_day_number(arriveBob))
        end = min(to_day_number(leaveAlice), to_day_number(leaveBob))
        return max(0, end - start + 1)
