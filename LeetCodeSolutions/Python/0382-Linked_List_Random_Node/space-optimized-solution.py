# SECOND SOLUTION
# Space-optimized solution (single pass through the list)
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:

        count = 0
        result = None
        tmpPtr = self.head

        while tmpPtr:
            count += 1
            if random.randint(1, count) == 1:
                result = tmpPtr.val
            tmpPtr = tmpPtr.next

        return result
