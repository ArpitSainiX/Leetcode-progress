// LeetCode Solution: Remove Duplicates From Sorted List Ii
// Submitted: 2026-07-27T14:27:25.033Z
// Language: Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        ref = dummy
        curr = head
         
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                ref.next = curr.next
            else:
                ref = ref.next
            curr = curr.next
        return dummy.next