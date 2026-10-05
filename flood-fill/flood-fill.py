// LeetCode Solution: Flood Fill
// Submitted: 2026-10-05T08:35:05.484Z
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
            
            if image[row][col] != original:
                return 

            image[row][col] = color

            f(row, col + 1)
            f(row, col - 1)
            f(row -1, col)
            f(row + 1, col)
        f(sr, sc)
        return image