# https://leetcode.com/problems/linked-list-random-node/submissions/912759525/
# Date of Submission: 2023-03-10

# Runtime: 75 ms, faster than 71.75% of Python3 online submissions for Linked List Random Node.
# Memory Usage: 17.3 MB, less than 73.23% of Python3 online submissions for Linked List Random Node.


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:

        count = 0
        tmpPtr = self.head

        # get length of list
        while tmpPtr:
            count += 1
            tmpPtr = tmpPtr.next

        tmpPtr = self.head
        # go to the i'th random node
        for i in range(0, random.randint(1, count)-1):
            tmpPtr = tmpPtr.next
        return tmpPtr.val
