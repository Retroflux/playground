# https://leetcode.com/problems/reverse-linked-list/submissions/913861716/
# Date of Submission: 2023-03-12

# Runtime: 35 ms, faster than 79.27% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.4 MB, less than 89.8% of Python3 online submissions for Reverse Linked List.

# Problem:
#  Given the head of a singly linked list, reverse the list, 
#  and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tmpPtr = head
        tmpStorage = []

        # store node values in list
        while tmpPtr:
            tmpStorage.append(tmpPtr.val)
            tmpPtr = tmpPtr.next

        # re-traverse the list, adding values in reverse order.
        tmpPtr = head
        for i in range(len(tmpStorage)-1, -1, -1):
            tmpPtr.val = tmpStorage[i]
            tmpPtr = tmpPtr.next

        return head
