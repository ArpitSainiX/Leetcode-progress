// LeetCode Solution: Palindrome Linked List
// Submitted: 2026-07-25T10:08:35.777Z
// Language: Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        return lst == lst[::-1]        









        #worst approach
        # reverse_arr = []
        # arr = []
        # temp = head
        # while temp:
        #     arr.append(temp.val)
        #     reverse_arr.append(temp.val)
        #     temp = temp.next
        

        # s1 = ""
        # s2 = ""
        # for i in range(len(arr)):
        #     s1 += str(arr[i])
        
        # for j in range(len(reverse_arr)-1,-1,-1):
        #     s2 += str(reverse_arr[j])
        
        # if s1 == s2:
        #     return True
        # return False