/*
https://leetcode.com/submissions/detail/718105603/
Date of Submission: 2022-06-09

Runtime: 6 ms, faster than 100% of C online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 7.2 MB, less than 71.36% of C online submissions for Two Sum II - Input Array Is Sorted.

*/

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize = 2;
    int leftPointer = 0;
    int rightPointer = numsSize-1;
    int * returnArray = malloc(sizeof(int)*(*returnSize));
    
    while((nums[leftPointer]+nums[rightPointer]) != target){
        if(nums[rightPointer] > target)                         {rightPointer--;}
        else if(nums[rightPointer] + nums[leftPointer] > target){rightPointer--;}
        else if(nums[rightPointer] + nums[leftPointer] < target){leftPointer++;}
    }
   
    returnArray[0] = leftPointer+1;
    returnArray[1] = rightPointer+1;

    return returnArray;
}

