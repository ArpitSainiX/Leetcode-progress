// LeetCode Solution: Car Pooling
// Submitted: 2026-10-30T10:11:40.619Z
// Language: Python3

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        diff = [0]*1001 

        for passengers, st, end in trips:
            diff[st] += passengers
            diff[end] -= passengers
        
        curr = 0
        
        for el in diff:
            curr += el
            if curr > capacity:
                return False
        return True