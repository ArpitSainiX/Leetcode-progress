// LeetCode Solution: Maximum Twin Sum Of A Linked List
// Submitted: 2026-07-27T13:31:07.696Z
// Language: Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, node: Optional[ListNode]) -> int:
        lst = []
        #appending the values in the lst.
        while node:
            lst.append(node.val)
            node = node.next
        
        #lst = [5,4,2,1]
        n = len(lst)
        first_half = lst[:n//2]
        second_half = lst[n//2:][::-1]
        # second_half.sort(reverse=True) #reversing the second_half

        max_sum = float('-inf')
        l,r = 0,0
        twin_sum = 0
        while l < len(first_half) and r < len(second_half):
            twin_sum = first_half[l] + second_half[r]
            l += 1 
            r += 1
            if twin_sum > max_sum:
                max_sum = twin_sum
            
        return max_sum


        

        
