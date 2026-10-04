// LeetCode Solution: Validate Binary Search Tree
// Submitted: 2026-10-04T15:24:03.033Z
// Language: Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        ans = []

        def dfs(node):
            if node is None:
                return 
            
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        arr = sorted(ans)
        return ans == arr