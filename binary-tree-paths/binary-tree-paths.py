// LeetCode Solution: Binary Tree Paths
// Submitted: 2026-10-09T13:55:33.960Z
// Language: Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        ans = []
        curr_path = []

        def backtrack(node):
            if node is None:
                return 
            curr_path.append(node.val)
            
            if node.left is None and node.right is None:
                ans.append("->".join(map(str, curr_path)))
            else:
                backtrack(node.left)
                backtrack(node.right)
            curr_path.pop()
        backtrack(root)
        return ans
            