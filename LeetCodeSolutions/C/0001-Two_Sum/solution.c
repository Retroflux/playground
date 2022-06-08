#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int sortFunc (const void * a, const void * b);
int* twoSum(int* nums, int numsSize, int target, int* returnSize);


int main(int argc, char const *argv[])
{
    /* code */
    int * returnArray=malloc(sizeof(int)*2);
    int nums[4] = {15,7,11,2};

    returnArray = twoSum(nums,sizeof(nums)/sizeof(int),13,returnArray);

    printf("%d + %d = %d\n",nums[returnArray[0]], nums[returnArray[1]],nums[returnArray[0]]+nums[returnArray[1]]);
    free(returnArray);
    return 0;
}


int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int leftPointer = 0;
    int rightPointer = numsSize-1;
    qsort(nums,numsSize,sizeof(int),sortFunc);
    
    
    while((nums[leftPointer]+nums[rightPointer]) != target){
        if(nums[rightPointer] > target)                         {rightPointer--;}
        else if(nums[rightPointer] + nums[leftPointer] > target){rightPointer--;}
        else if(nums[rightPointer] + nums[leftPointer] < target){leftPointer++;}
    }
   
    returnSize[0]= leftPointer;
    returnSize[1]= rightPointer;

    return returnSize;
}


//Adapted from https://www.tutorialspoint.com/c_standard_library/c_function_qsort.htm
int sortFunc (const void * a, const void * b) {
   return (*(int*)a - *(int*)b);
}