# https://leetcode.com/problems/middle-of-the-linked-list/submissions/914581005/
# Date of Submission: 2023-03-13

# Runtime: 27 ms, faster than 90.42% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.8 MB, less than 96.48% of Python3 online submissions for Middle of the Linked List.

# Problem:
#  Given the head of a singly linked list, return the middle node of the linked list.
#  If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middleNode = head
        endFinder = head.next

        if endFinder == None:
            return head

        while endFinder != None:
            endFinder = endFinder.next
            middleNode = middleNode.next
            if endFinder == None:
                return middleNode
            endFinder = endFinder.next
        return middleNode 