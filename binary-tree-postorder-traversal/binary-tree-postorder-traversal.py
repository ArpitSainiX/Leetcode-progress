// LeetCode Solution: Binary Tree Postorder Traversal
// Submitted: 2026-09-29T12:49:22.950Z
// Language: Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []

        def solve(node):
            if node is None:
                return 
            
            solve(node.left)
            solve(node.right)
            ans.append(node.val)
        solve(root)
        return ans