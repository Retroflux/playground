#include <stdio.h>
#include <stdlib.h>

/*
Date of Submission: 2022-06-08

Note that this code is not what was submitted. There was no 
reason to push for linear time on this submission when the
qsort can do it in nlogn time; If you want a linear time 
solution for this, you can hire me.

*/
int sortFunc (const void * a, const void * b);
int* twoSum(int* nums, int numsSize, int target, int* returnSize);


int main(int argc, char const *argv[])
{
    /* code */
    int * returnSize=malloc(sizeof(int)*1);
    int nums[4] = {15,7,11,2};
    int * returnArray;

    returnArray = twoSum(nums,sizeof(nums)/sizeof(int),13,returnSize);

    printf("%d + %d = %d\n",nums[returnArray[0]], nums[returnArray[1]],nums[returnArray[0]]+nums[returnArray[1]]);
    free(returnArray);
    return 0;
}


int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize = 2;
    int leftPointer = 0;
    int rightPointer = numsSize-1;
    qsort(nums,numsSize,sizeof(int),sortFunc);
    int * returnArray = malloc(sizeof(int)*(*returnSize));
    
    while((nums[leftPointer]+nums[rightPointer]) != target){
        if(nums[rightPointer] > target)                         {rightPointer--;}
        else if(nums[rightPointer] + nums[leftPointer] > target){rightPointer--;}
        else if(nums[rightPointer] + nums[leftPointer] < target){leftPointer++;}
    }
   
    returnArray[0] = leftPointer;
    returnArray[1] = rightPointer;

    return returnArray;
}


//Adapted from https://www.tutorialspoint.com/c_standard_library/c_function_qsort.htm
int sortFunc (const void * a, const void * b) {
   return (*(int*)a - *(int*)b);
}