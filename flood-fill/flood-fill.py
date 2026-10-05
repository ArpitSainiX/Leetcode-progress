// LeetCode Solution: Flood Fill
// Submitted: 2026-10-05T08:37:36.686Z
// Language: Python3

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m = len(image) #row size
        n = len(image[0]) #col size

        original = image[sr][sc]

        if original == color:
            return image
        
        def f(row, col):
            if row < 0 or col < 0 or row >= m or col >= n:
                return 
            
            #for the visited row and col preventing.
            if image[row][col] != original:
                return 

            #coloring
            image[row][col] = color

            #going right
            f(row, col + 1)

            #going left
            f(row, col - 1)

            #going up
            f(row -1, col)

            #going down
            f(row + 1, col)
            
        f(sr, sc)
        return image