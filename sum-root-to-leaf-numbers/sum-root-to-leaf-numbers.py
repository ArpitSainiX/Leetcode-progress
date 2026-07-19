// LeetCode Solution: Sum Root To Leaf Numbers
// Submitted: 2026-07-19T07:55:47.730Z
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
            if node == None:
                return None
            
            num = num * 10 + node.val

            if node.left == None and node.right == None:
                return num
            
            return dfs(node.left, num) + dfs(node.right, num)
        return dfs(root, 0)