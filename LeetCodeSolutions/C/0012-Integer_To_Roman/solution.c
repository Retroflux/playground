#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
https://leetcode.com/submissions/detail/717361983/
Date of Submission: 2022-06-08

Runtime: 4 ms, faster than 82.36% of C online submissions for Integer to Roman.
Memory Usage: 5.8 MB, less than 92.07% of C online submissions for Integer to Roman.

*/

int isolateLeftDigit(int numRemaining);
char * intToRoman(int num);

int main() {
  printf("%s\n", intToRoman(102)); 
  printf("%s\n", intToRoman(3888)); 
  printf("%s\n", intToRoman(33)); 
  printf("%s\n", intToRoman(1994)); 

  return 0;
}


//Largest string between [1,3999] would be 3888 (MMMDCCCLXXXVIII)

char * intToRoman(int num){
    char * romanEquivalent= (char*)calloc(16,sizeof(char));
    int stringPos = 0;
    int numericValue[7] = {1000,500,100,50,10,5,1};
    char romanValue[8] = {'M','D','C','L','X','V','I'};   

    while(num > 999){
        strcpy(&romanEquivalent[stringPos],"M");
        stringPos++;
        num-=1000;
    }
    
    for (int j=1; j<7;j++){
        while (num >= numericValue[j]){
            if(isolateLeftDigit(num) == 9){
                strcpy(&romanEquivalent[stringPos],&romanValue[j+1]);
                strcpy(&romanEquivalent[stringPos+1],&romanValue[j-1]);
                num-=numericValue[j+1] * 9;
                stringPos+=2;
            }
            else if(isolateLeftDigit(num) == 4){
                strcpy(&romanEquivalent[stringPos],&romanValue[j]);
                strcpy(&romanEquivalent[stringPos+1],&romanValue[j-1]);
                num-=numericValue[j-1] * 0.8;
                stringPos+=2;
            }else{
                strcpy(&romanEquivalent[stringPos],&romanValue[j]);
                stringPos++;
                num -= numericValue[j];   
            }
        }
    }
    romanEquivalent[stringPos] = '\0';
    return romanEquivalent;   
}


int isolateLeftDigit(int numRemaining){
    if(numRemaining < 10){
        return numRemaining;
    }
    while(numRemaining >=10){
        numRemaining/=10;
    }
    return numRemaining;
}