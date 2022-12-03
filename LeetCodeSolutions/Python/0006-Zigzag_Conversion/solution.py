# https://leetcode.com/submissions/detail/719256552/
# Date of Submission: 2022-06-10

# Runtime: 70 ms, faster than 71.71% of Python3 online submissions for Zigzag Conversion.
# Memory Usage: 14 MB, less than 50.73% of Python3 online submissions for Zigzag Conversion.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction = 0 #up or down
        positionalDictionary = dict()
        currRow = 0
        currCol = 0
        
        if(numRows == 1):
            return s

        for letter in s:
            positionalValue = currCol + 1001*numRows*currRow
            positionalDictionary[positionalValue] = letter
            #boundary check for direction flipping
            if(direction == 0 and currRow == numRows-1):
                direction = 1
            elif(direction == 1 and currRow == 0):
                direction = 0
                
            if (direction == 0): #down part of zigzag
                currRow+=1
            elif(direction == 1):#up part of zigzag
                currRow-=1
                currCol+=1

        sortedDict = dict(sorted(positionalDictionary.items()))
        return ''.join(sortedDict.values())
        