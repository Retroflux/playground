class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        visitedNodes = list()
        visitedNodes.append(head)

        tmpPtr = head
        while tmpPtr.next is not None:
            if tmpPtr.next in visitedNodes:
                return tmpPtr.next
            tmpPtr = tmpPtr.next
            visitedNodes.append(tmpPtr)

        return None
