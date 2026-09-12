// LeetCode Solution: Find Mode In Binary Search Tree
// Submitted: 2026-09-12T11:37:09.734Z
// Language: Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        dfs(root)

        #now the lst is -> [1,2,2]
        fq = {}

        for el in lst:
            if el in fq:
                fq[el] += 1
            else:
                fq[el] = 1

        max_freq = max(fq.values())

        return [val for val, count in fq.items() if count == max_freq]
        