// LeetCode Solution: Sum Root To Leaf Numbers
// Submitted: 2026-07-19T07:57:38.554Z
// Language: Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num):
            if not node:
                return None
            
            num = num * 10 + node.val

            if not node.left and not node.right:
                return num
            
            return dfs(node.left, num) + dfs(node.right, num)
        return dfs(root, 0)