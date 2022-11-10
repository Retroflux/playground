/*
https://leetcode.com/submissions/detail/726059614/
Date of Submission: 2022-06-19

Runtime: 0 ms, faster than 100.00% of C online submissions for String to Integer (atoi).
Memory Usage: 5.6 MB, less than 85.18% of C online submissions for String to Integer (atoi).
*/

int frontStrip(char * s, int sLen);
int sumCharRange(char * s, int stripAmount, int rangeEnd);

int myAtoi(char * s){

    int sLen = strlen(s);
    if (sLen == 0){
        return 0;
    }

    int stripAmount = frontStrip(s, sLen);
    int negationFlag = 0;
    int summation = 0;
    int numberLength = 0;
    int leadingZeroesFlag = 0;

    //check for leading sign (positive or negative)
    if(s[stripAmount] == '-'){
        negationFlag = 1;
        stripAmount++;

    }else if(s[stripAmount] == '+'){
        stripAmount++;
    }

    //get length of number, keeping in mind that leading zeroes do not count
    for(int i = stripAmount; i < sLen; i++){
        if (!isdigit(s[i])){break;}
        else{
            if(s[i] == '0' && leadingZeroesFlag == 0){
                stripAmount++;
            }
            if(leadingZeroesFlag == 0 && s[i] != '0'){
                leadingZeroesFlag++;
            }
            if(leadingZeroesFlag){
                numberLength++;
            }
        }
    }
    //different cases for different number lengths; else case is the overflow boundary and is the most complex.
    if(numberLength > 10 && negationFlag){return -2147483648;}
    else if(numberLength > 10 && (!negationFlag)){return 2147483647;}
    else if(numberLength < 10){summation = sumCharRange(s, stripAmount, stripAmount+numberLength);}
    else{
        //sum all numbers in the range EXCEPT the final one (numberLength-1)
        summation = sumCharRange(s, stripAmount, (stripAmount+numberLength-1));
        int finalDigit = s[stripAmount+numberLength-1] - '0'; //final digit stored here

        //if the composite of the summation and the 1's col digit would overflow, return +/- maxVal
        if((finalDigit > 7+negationFlag && summation >= 214748364) || summation > 214748364){
            if(negationFlag){
                return -2147483648;
            }else{
                return 2147483647;
            }
        }
        //handle negationFlag for summation of final digit
        if(negationFlag){
            summation = (summation *-10) + finalDigit*-1;
        }else{
            summation = (summation *10) + finalDigit;
        }
        return summation;
    }
    if(negationFlag){
        summation *= -1;
    }

    return summation;
}

//sum any range of integer digits within the integer range
int sumCharRange(char * s, int stripAmount, int rangeEnd){
    int summation = 0;
    int currInt = 0;
    for(int i = stripAmount; i< rangeEnd; i++){
        currInt = s[i] - '0';
        summation = summation * 10 + currInt;
    }
    return summation;
}

//strips whitespace, returns index of first non-whitespace index
int frontStrip(char * s, int sLen){
    int stripAmount = 0;
    for (int i = 0; i < sLen; i++){
        if(s[i] == ' '){
            stripAmount++;
        }else{
            break;
        }
    }
    return stripAmount;
}

//sum any range of integer digits within the integer range
int sumCharRange(char * s, int stripAmount, int rangeEnd){
    int summation = 0;
    int currInt = 0;
    for(int i = stripAmount; i< rangeEnd; i++){
        currInt = s[i] - '0';
        summation = summation * 10 + currInt;
    }
    return summation;
}

//strips whitespace, returns index of first non-whitespace index
int frontStrip(char * s, int sLen){
    int stripAmount = 0;
    for (int i = 0; i < sLen; i++){
        if(s[i] == ' '){
            stripAmount++;
        }else{
            break;
        }
    }
    return stripAmount;
}