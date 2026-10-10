// LeetCode Solution: Rotate List
// Submitted: 2026-10-10T15:58:04.014Z
// Language: Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        
        if not head:
            return None
        if head.next is None:
            return head
        
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        
        curr.next = head
        k = k % n
        k = n - k - 1
        
        curr = head
        for i in range(k):
            curr = curr.next
        ret = curr.next
        curr.next = None
        return ret


        


        
