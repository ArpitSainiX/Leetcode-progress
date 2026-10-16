// LeetCode Solution: Same Tree
// Submitted: 2026-10-16T10:39:59.344Z
// Language: Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        arr1 = []
        arr2 = []

        def firstTree(node1):
            if node1 is None:
                arr1.append(None)
                return 
            firstTree(node1.left)
            arr1.append(node1.val)
            firstTree(node1.right)
        firstTree(p)

        def secondTree(node2):
            if node2 is None:
                arr2.append(None)
                return
            
            secondTree(node2.left)
            arr2.append(node2.val)
            secondTree(node2.right)
        secondTree(q)

        if arr1 == arr2:
            return True
        return False