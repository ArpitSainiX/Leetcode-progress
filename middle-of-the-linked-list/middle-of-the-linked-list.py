// LeetCode Solution: Middle Of The Linked List
// Submitted: 2026-10-11T13:53:53.868Z
// Language: Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow