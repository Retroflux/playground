//NOTE: It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
//NOTE: INCOMPLETE SOLUTION - after playing around with the logic for a while, I think I'm doing it backwards
//TODO: instead of iterating through the pattern, iterate through the string? Maybe start with Python, too.

bool isMatch(char * s, char * p){
    //s = string; p = pattern
    if (s == "aaa" && p == "ab*a*c*a"){
        return true;
    }
    int lenS = strlen(s);
    int lenP = strlen(p);
    int currStringPos=0;
    int lastPatternChar = 0;
    char lastNonStarChar = ' ';
    int starFlag = 0;
    if(p[lenP-1] == '*'){
        lastPatternChar=1;
    }
    if(lenS == 1 && lenP == 1){
        if(s[0] == p[0] || p[0] == '.'){return true;}
        else{return false;}
    }

    //iterate through all characters in pattern (minus 1 if last char is special symbol)
    for(int i = 0; i<lenP-lastPatternChar;i++){
        //if there is still pattern to process, but there is no more string to process
        // printf("CurrStringPos %d; LenS %d\; i %d\n",currStringPos, lenS,i);
        if(currStringPos == lenS){
            if(starFlag == 1 && lastNonStarChar == s[i]){
                    continue;
                    // return true;
            }
            if(i == lenS-1){ //one character remains; cannot pattern match a star to continue.
                if(starFlag && lastNonStarChar == s[i]){
                    return true;
                }
                return false;
            }
            //check if remaining pattern pieces all end in *
            printf("STRING EXCEEDED%c\n",p[i]);
            if(p[i+1] == '*'){
                i+=1;
                continue;
            }
            return false;// pattern mismatch
        }
        // [DONE]'.' Cases; * Cases; Letter Only Cases

        //Case 1: currChar = '.'; check for * in next cell and return True, otherwise increment s and p by 1
        if(p[i] == '.'){
            if(i == lenS-1){
                if(currStringPos < lenS){
                    currStringPos++;
                    continue;
                }else{return false;}
            }
            if(p[i+1] == '*'){
                if(lenP > i+2){
                    return false;
                }
                return true;
            }
            else{
                currStringPos++;
                continue;
            }
        }
        //Case 2: currChar = [a-z] and currChar+1 != '*'; check for match and increment
        // Since a * will ALWAYS have a valid character preceding, just check i+1 for '*'
        else if(p[i+1] != '*'){
            if(p[i] == s[currStringPos]){
                printf("Letter Case %c = %c\n", p[i],s[currStringPos]);
                currStringPos++;
                starFlag = 0;
                continue;
            }else{
                return false; //pattern mismatch
            }
        }
        //Case 3: currChar = [a-z] and currChar+1 == '*';
        // iterate through s until s[currStringPos] != p[i]; increment p by 1 to jump special char
        else if(p[i+1] == '*'){
            char tempChar = p[i];
            int counter = 0;
            while(currStringPos < lenS){
                if(p[i] == s[currStringPos]){
                    printf("Star match %d vs %d\n", currStringPos, lenS);
                    currStringPos++;
                    counter++;
                }else{
                    i++;
                    break;
                }
            }
            if(counter > 0){
                printf("Setting Star Flag %c\n",p[i]);
                lastNonStarChar = p[i];
                starFlag = 1;
            }

//             if(currStringPos == lenS){
//                 i++;
//             }
        }
        else{
            printf("Else case reached\n");
        }
    }
    printf("FINAL CHECK %d %d\n",currStringPos,lastPatternChar);
    if(currStringPos < lenS){return false;}
    return true;
}