// LeetCode Solution: Swapping Nodes In A Linked List
// Submitted: 2026-07-29T05:56:59.039Z
// Language: Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # temp = head
        first = last = head
        for i in range(1,k):
            first = first.next
        
        nullChecker = first
        while nullChecker.next:
            last = last.next
            nullChecker = nullChecker.next
        first.val, last.val = last.val, first.val
        return head