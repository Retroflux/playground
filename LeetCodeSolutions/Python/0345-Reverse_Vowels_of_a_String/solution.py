# https://leetcode.com/submissions/detail/719233334/
# Date of Submission: 2022-06-10

# Runtime: 58 ms, faster than 84.14% of Python3 online submissions for Reverse Vowels of a String.
# Memory Usage: 15.1 MB, less than 58.34% of Python3 online submissions for Reverse Vowels of a String.

class Solution:

    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u"]
        vowelFlag = 0
        for vowel in vowels:
            if vowel in s.lower():
                vowelFlag = 1
        if vowelFlag == 0:
            return s
        leftPtr = 0
        rightPtr = len(s)-1
        sList = list(s)
        
        while(leftPtr < rightPtr):
            while(not(sList[leftPtr].lower() in vowels) and leftPtr < rightPtr):
                leftPtr+=1
            while(not(sList[rightPtr].lower() in vowels) and leftPtr < rightPtr):
                rightPtr-=1
            temp = sList[leftPtr]
            sList[leftPtr] = sList[rightPtr]
            sList[rightPtr] = temp
            leftPtr+=1
            rightPtr-=1

        return ''.join(sList)