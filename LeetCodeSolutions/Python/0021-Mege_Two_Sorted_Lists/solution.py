# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/submissions/detail/743858145/
# Date of Submission: 2022-07-10

# Runtime: 41 ms, faster than 88.01% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.9 MB, less than 78.98% of Python3 online submissions for Merge Two Sorted Lists.


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if (list1 == None or list2 == None):
            if (list1 == None):
                return list2
            elif (list2 == None):
                return list1

        outputList = []

        if (list1.val <= list2.val):
            outputList = ListNode(list1.val)
            list1 = list1.next
        else:
            outputList = ListNode(list2.val)
            list2 = list2.next

        currPost = outputList

        while (list1 != None and list2 != None):
            if (list1.val <= list2.val):
                currPost.next = list1
                list1 = list1.next
            else:
                currPost.next = list2
                list2 = list2.next
            currPost = currPost.next

        if (list1 == None):  # empty out list2
            while (list2 != None):
                currPost.next = list2
                currPost = currPost.next
                list2 = list2.next
        else:  # empty out list1
            while (list1 != None):
                currPost.next = list1
                currPost = currPost.next
                list1 = list1.next

        return outputList