// LeetCode Solution: Delete Node In A Linked List
// Submitted: 2026-09-30T08:23:25.507Z
// Language: Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None or node.next is None:
            return
        node.val = node.next.val
        node.next = node.next.next


        