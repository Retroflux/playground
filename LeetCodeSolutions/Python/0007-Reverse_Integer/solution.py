# https://leetcode.com/submissions/detail/718457400/
# Date of Submission: 2022-06-09

# Runtime: 38 ms, faster than 76.09% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.8 MB, less than 96.91% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:
        
        reversed = ""
        signFlag = 0
        x = str(x)
        if (x[0] == "-"):
            signFlag = 1
            x = x[1:]
        #check overflow cases
        if (len(x) == 10):
            firstDigit = int(x[-1])
            temp = x[-2::-1]
            if(firstDigit > 1 and int(temp) > 147483647 and signFlag == 0):
                return 0
            elif(firstDigit > 1 and int(temp) > 147483648 and signFlag == 1):
                return 0
        #normal case 
        reversed = x[::-1]
        if(signFlag):
            reversed = "-" + reversed
        return int(reversed)