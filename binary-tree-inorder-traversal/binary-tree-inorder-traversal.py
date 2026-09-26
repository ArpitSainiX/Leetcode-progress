// LeetCode Solution: Binary Tree Inorder Traversal
// Submitted: 2026-09-26T14:14:46.844Z
// Language: Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []

        def solve(node):
            if node == None:
                return 
            
            solve(node.left)
            ans.append(node.val)
            solve(node.right)
        solve(root)
        return ans