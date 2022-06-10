class Solution:
    def longestPalindrome(self, s: str) -> str:

        if(len(s) == 1):
            return s
        elif (len(s) == 2 and s[0] != s[1]):
            return s[0]
        elif(len(s) == 2 and s[0] == s[1]):
            return s
        i = 0
        j = 0
        n = len(s)-1
        maxSubstring = 1
        subStringPos = 0
        
        #TODO Extremely long strings of potential substrings take too long. It might be best to convert the string into a more compact design (ex. aaaa = a4).
        for i in range(0,n):
            if(n-i < maxSubstring):
                break
            for j in range(n,-1,-1):
                if(j - i < maxSubstring): #if there's no chance for the substring to be found, break 
                    break
                currentSubstringLength = 0
                offset= 0
                while(1):
                    if(s[i+offset] != s[j-offset]):
                        break
                    if j-offset < i+offset: #even distance between start and endpoints
                        if (currentSubstringLength > maxSubstring):
                            maxSubstring = currentSubstringLength
                            subStringPos = i
                        break     
                    elif j-offset == i+offset:#odd distance between start and endpoints
                        currentSubstringLength+=1
                        if (currentSubstringLength > maxSubstring):
                            maxSubstring = currentSubstringLength
                            subStringPos = i
                        break                
                    
                    currentSubstringLength += 2
                    offset+=1
        return s[subStringPos:subStringPos+maxSubstring]
    
        