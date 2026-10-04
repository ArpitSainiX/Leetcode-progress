// LeetCode Solution: Validate Binary Search Tree
// Submitted: 2026-10-04T15:29:22.333Z
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
                return None
            
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)

        arr = sorted(ans)
        for i in range(1,len(ans)):
            if ans[i] == ans[i-1]:
                return False
        if ans != arr:
            return False
        return True