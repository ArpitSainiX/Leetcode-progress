// LeetCode Solution: Delete Nodes From Linked List Present In Array
// Submitted: 2026-10-02T15:58:25.410Z
// Language: Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set01 = set(nums)
        

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr.next:
            if curr.next.val in set01:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


