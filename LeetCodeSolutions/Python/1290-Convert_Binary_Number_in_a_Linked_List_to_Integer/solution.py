# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/918234597/

# Runtime: 26 ms, faster than 93.69% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 13.8 MB, less than 42.40% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
#

# Problem:
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# The most significant bit is at the head of the linked list.

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        string = ""
        output = 0
        while head:
            string += str(head.val)
            head = head.next
        stringLength = len(string)

        for i in range(0, stringLength):
            if string[i] == "1":
                output += 2 ** (stringLength-i-1)

        return output
