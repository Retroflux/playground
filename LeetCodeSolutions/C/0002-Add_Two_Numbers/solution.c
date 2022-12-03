/**
# https://leetcode.com/submissions/detail/719705127/
# Date of Submission: 2022-06-11

# Runtime: 26 ms, faster than 20.81% of C online submissions for Add Two Numbers.
# Memory Usage: 7 MB, less than 98.82% of C online submissions for Add Two Numbers.


NOTE: if runtime is important, removing and re-integrating the getListLength function
can reduce the runtime by 14ms with no discernable increase to memory usage; however,
in terms of readability, it becomes much less friendly.

See: https://leetcode.com/submissions/detail/719698188/ for more details.
*/



/*
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
*/


void updateNodes(struct ListNode * bigList, struct ListNode *smallList);
void pushCarryForward(struct ListNode * bigList);
int getListLength(struct ListNode * list);


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode * listOnePtr = l1;
    struct ListNode * listTwoPtr = l2;
    int listOneLen = getListLength(l1);
    int listTwoLen = getListLength(l2);
    
    //if list one is bigger or equal, add to it 
    if(listOneLen >= listTwoLen){
        updateNodes(l1,l2);
        return l1;
    }
    else{
        updateNodes(l2,l1);
        return l2;
    }
}

int getListLength(struct ListNode * list){
    int listLength = 0;
     while(list !=NULL){
        listLength++;
        list=list->next;
    }
    return listLength;
}

void updateNodes(struct ListNode * bigList, struct ListNode *smallList){
    while (smallList!=NULL){
        bigList->val += smallList->val;
        pushCarryForward(bigList);
        bigList = bigList->next;
        smallList = smallList->next;
    }
}
void pushCarryForward(struct ListNode * bigList){
    while(bigList!=NULL){
        if (bigList->val > 9){
            if(bigList->next == NULL){
                struct ListNode * tempPtr = malloc(sizeof(struct ListNode));
                tempPtr->val = 0;
                tempPtr->next = bigList->next;
                bigList->next = tempPtr;
            }
            bigList->next->val +=1;
            bigList->val = bigList->val - 10;
        }
        bigList=bigList->next;
    }
    return;
}