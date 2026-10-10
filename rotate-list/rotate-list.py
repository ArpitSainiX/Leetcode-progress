// LeetCode Solution: Rotate List
// Submitted: 2026-10-10T15:52:14.082Z
// Language: Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head
        
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        
        k = k%n
        if k == 0:
            return head

        #make circular
        tail.next = head

        steps = n-k
        new_tail = head

        for _ in range(steps-1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head


        


        


        
