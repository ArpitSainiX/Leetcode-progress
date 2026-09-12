// LeetCode Solution: Find Mode In Binary Search Tree
// Submitted: 2026-09-12T05:48:12.784Z
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

        if len(lst) == 1:
            return lst
        #if length is greater than 1

        freq = {}
        for el in lst:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1
        
        keys, value = [], []

        for k, v in freq.items():
            keys.append(k)
            value.append(v)

        max_elem_val = max(value)
        max_elem_index = value.index(max_elem_val)

        return [keys[max_elem_index]]