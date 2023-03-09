class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fastPtr = head
        slowPtr = head
        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            if fastPtr == slowPtr:
                slowPtr = head
                while slowPtr != fastPtr:
                    fastPtr = fastPtr.next
                    slowPtr = slowPtr.next
                return slowPtr
        return None
