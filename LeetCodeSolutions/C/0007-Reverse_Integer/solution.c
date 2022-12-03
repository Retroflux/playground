/*
https://leetcode.com/submissions/detail/718480228/
Date of Submission: 2022-06-09

Runtime: 0 ms, faster than 100% of C online submissions for Reverse Integer.
Memory Usage: 5.8 MB, less than 24% of C online submissions for Reverse Integer.

NOTE: Requires math.h and stdio.h to run outside of LeetCode */
int reverse(int x){
    int reversed = 0;
    int counter = 0;
    int signFlag = 0;
    

   
    int firstDigit = x % 10;
    firstDigit = abs(firstDigit);
    x = x/10; //remove "leftmost" resultant digit
    
    if(x < 0){
        signFlag = 1;
        x=abs(x);
    }
    
    //Create output number, minus its leftmost digit
    while(x > 0){
        reversed *=10;
        reversed = reversed + x % 10;
        x = x/10;
        counter++;
    }
    //overflow edge case checking
    //overflow can only occur if 9 (+1 removed) digits exist in x.
    if (counter == 9){
        if (firstDigit > 1 && reversed > 147483647 && signFlag == 0){
            return 0;
        }
        if(firstDigit > 1 && reversed > 147483648 && signFlag == 1){
            return 0;
        }
    }
    
    //base case 
    if(signFlag){
        reversed = -1 * (reversed + (int)(pow(10,counter))*firstDigit);
    }else{
        reversed = reversed + (int)(pow(10,counter))*firstDigit;
    } 
    
    return reversed;
}