
# https://leetcode.com/submissions/detail/718951041/
# Date of Submission: 2022-06-10

# Runtime: 293 ms, faster than 94.14% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.9 MB, less than 90.90% of Python3 online submissions for Longest Palindromic Substring.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)-1
        maxSubstring = 1
        subStringPos = 0
        currentSubstringLength = 0

        #odd substring length check
        for i in range(0,n):
            if(min(i,n-i)*2+1 <= maxSubstring):
                continue
            currentSubstringLength = 1   
            for j in range(1,min(i,n-i)+1):
                if(s[i-j] == s[i+j]): #the palindrome expands to the left and right of the midpoint by 1
                    currentSubstringLength+=2
                else: #there is a mismatch in letters
                    break
            if(currentSubstringLength > maxSubstring):#update maxSubstring and position if necessary
                maxSubstring = currentSubstringLength
                subStringPos = int(i-((currentSubstringLength-1)/2))

        #even substring length check
        for i in range(0,n):
            if (s[i] != s[i+1]):
                continue
            elif(min(i,n-1-i)*2+2 <= maxSubstring):
                continue
            
            currentSubstringLength = 2
            for j in range(1,min(i,n-1-i)+1):
                if(s[i-j] == s[i+1+j]):
                    currentSubstringLength+=2 #the palindrome expands to the left and right of the midpoint by 1
                else:
                    break#there is a mismatch in letters
            if(currentSubstringLength > maxSubstring): #update maxSubstring and position if necessary
                maxSubstring = currentSubstringLength
                subStringPos = int(i-((currentSubstringLength-2)/2))
        return s[subStringPos:subStringPos+maxSubstring]
