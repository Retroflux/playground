# https://leetcode.com/problems/can-place-flowers/submissions/918833444/
# Date of Submission: 2023-03-20

# Runtime: 125 ms, faster than 9.90% of Python3 online submissions for Sort Integers by the Number of 1 Bits.
# Memory Usage: 14.1Mb, less than 71.55% of Python3 online submissions for Sort Integers by the Number of 1 Bits.

#Problem: 



#To anyone that reads this, you can also do this one line and have the same results in half the time:
#        return sorted(arr, key=lambda x: [bin(x).count('1'), x])
#I'm not changing my solution because it's just more memory optimized (or the same), and twice as slow LOL
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return arr

        dictOfBinaryBitCounts = dict()
        for number in arr:
            numOnes = self.countOnes(number)

            if not numOnes in dictOfBinaryBitCounts:
                dictOfBinaryBitCounts[numOnes] = []
            dictOfBinaryBitCounts[numOnes].append(number)
        
        outputList = self.createOutputList(dictOfBinaryBitCounts)
        return outputList
    def createOutputList(self,dictOfBinaryBitCounts):
        outputList = list()
        dictKeys = list(dictOfBinaryBitCounts.keys())
        dictKeys.sort()

        for key in dictKeys:
            dictOfBinaryBitCounts[key].sort()
            outputList += dictOfBinaryBitCounts[key]

        return outputList

    def countOnes(self, number):
        if number == 0:
            return 0
        
        numOnes = 0
        biggestPowTwo = floor(log2(number))
        while number > 0: 
            if number >= 2**biggestPowTwo:
                number-= 2**biggestPowTwo
                numOnes += 1
            biggestPowTwo-=1
        return numOnes