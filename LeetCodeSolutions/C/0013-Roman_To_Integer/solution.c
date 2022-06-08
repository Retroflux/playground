/*

https://leetcode.com/submissions/detail/716960928/
Date of Submission: 2022-06-07

Runtime: 0 ms, faster than 100.00% of C online submissions for Roman to Integer.
Memory Usage: 5.8 MB, less than 84.89% of C online submissions for Roman to Integer.

*/

int convertToNumeric(char currentChar);

int romanToInt(char * s){

    if (s == NULL || strlen(s) == 0){
        return 0;
    }
    
    int currentChar = 0;
    int previousChar = convertToNumeric(s[0]);
    int sum = 0;
    int convertedVal = 0;
    
    for(int i=0;i<strlen(s);i++){
        currentChar = convertToNumeric(s[i]);
        if(previousChar < currentChar){
            sum -= previousChar*2;
        }
        sum+=currentChar;
        previousChar=currentChar;
    }
    return sum;
}


int convertToNumeric(char currentChar){
    if (currentChar == 'M')     {return 1000;}
    else if (currentChar == 'C'){return 100;}
    else if (currentChar == 'X'){return 10;}
    else if (currentChar == 'I'){return 1;}
    else if (currentChar == 'V'){return 5;}
    else if (currentChar == 'L'){return 50;}
    else return 500;    
}