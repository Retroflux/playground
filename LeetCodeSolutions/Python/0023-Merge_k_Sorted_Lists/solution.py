# https://leetcode.com/problems/merge-k-sorted-lists/submissions/911601172/
# Date of Submission: 2023-03-08
#
# Memory Optimized solution
#
# Runtime: 4298 ms, faster than 9% of Python3 online submissions for Merge_k_Sorted_Lists.
# Memory Usage: 17.5 MB, less than 89.64% of Python3 online submissions for Merge_k_Sorted_Lists.
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedList = None
        tmpPtr = mergedList
        currMin = 0
        currBest = 0
        if len(lists) == 0:
            return None
        while len(lists) > 0:
            currMin = 100000
            currBest = -1
            for i in range (0,len(lists)):
                if lists[i] is not None:
                    if lists[i].val < currMin:
                        currMin = lists[i].val
                        currBest = i
            if currBest == -1:
                break
            #base case
            if(mergedList is None):
                mergedList = lists[currBest]
                lists[currBest] = lists[currBest].next
                mergedList.next = None
                tmpPtr = mergedList
            else: #shift lowest val to mergedList
                tmpPtr.next = lists[currBest]
                lists[currBest] = lists[currBest].next
                tmpPtr=tmpPtr.next
                tmpPtr.next=None
            if lists[currBest] is None:
                del lists[currBest]

        return mergedList