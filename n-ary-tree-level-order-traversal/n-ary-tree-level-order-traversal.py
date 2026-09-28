// LeetCode Solution: N Ary Tree Level Order Traversal
// Submitted: 2026-09-28T08:19:34.394Z
// Language: Python3

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, node: 'Node') -> List[List[int]]:
        ans = []
        if node is None:
            return []
        queue = deque([node])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children or []:
                    queue.append(child)
            ans.append(level)
        return ans