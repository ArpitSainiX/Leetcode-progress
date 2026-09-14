// LeetCode Solution: Rectangle Overlap
// Submitted: 2026-09-14T05:04:49.779Z
// Language: Python3

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2 = rec1
        x3,y3,x4,y4 = rec2
        
        if (x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3):
            return True
        return False
        