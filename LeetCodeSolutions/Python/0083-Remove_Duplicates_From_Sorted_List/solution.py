# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/928639055/
# Date of Submission: 2023-04-05

# Runtime: 33 ms, faster than 98% of Python3 online submissions for Remove Duplicates From Sorted List.
# Memory Usage: 13.8 MB, less than 96.10% of Python3 online submissions for Remove Duplicates From Sorted List.
#
# Problem: Given the head of a sorted linked list, delete all duplicates such that each element
#  appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        listPtr = head

        while listPtr.next != None:
            if listPtr.val == listPtr.next.val:
                if listPtr.next.next is None:
                    listPtr.next = None
                else:
                    listPtr.next = listPtr.next.next
            else:
                listPtr = listPtr.next

        return head
