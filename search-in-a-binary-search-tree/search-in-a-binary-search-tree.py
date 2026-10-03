// LeetCode Solution: Search In A Binary Search Tree
// Submitted: 2026-10-03T16:50:06.345Z
// Language: Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def dfs(node):
            if node is None:
                return None
            
            if node.val == val:
                return node
            elif val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        return dfs(root)
            
