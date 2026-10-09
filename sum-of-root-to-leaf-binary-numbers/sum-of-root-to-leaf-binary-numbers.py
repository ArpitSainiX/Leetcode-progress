// LeetCode Solution: Sum Of Root To Leaf Binary Numbers
// Submitted: 2026-10-09T14:16:52.600Z
// Language: Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        ans, curr_path = [], []

        def backtrack(node):
            if node is None:
                return 
            curr_path.append(node.val)

            if node.left is None and node.right is None:
                ans.append("".join(map(str, curr_path)))
            
            else:
                backtrack(node.left)
                backtrack(node.right)
            curr_path.pop()
        backtrack(root)

        return sum(int(s, 2) for s in ans)