/*
https://leetcode.com/submissions/detail/718309095/
Date of Submission: 2022-06-09

Runtime: 6 ms, faster than 88.13% of C online submissions for Running Sum of 1d Array.
Memory Usage: 6.6 MB, less than 98.85% of C online submissions for Running Sum of 1d Array.*/

int* runningSum(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;
    
    for(int i = 1; i<numsSize; i++){
        nums[i] += nums[i-1];
    }  
    return nums;
}