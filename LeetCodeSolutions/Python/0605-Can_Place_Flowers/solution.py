# https://leetcode.com/problems/can-place-flowers/submissions/918833444/
# Date of Submission: 2023-03-20

# Runtime: 187 ms, faster than 18.54% of Python3 online submissions for Can Place Flowers.
# Memory Usage: 14.5Mb, less than 20.94% of Python3 online submissions for Can Place Flowers.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        for i in range(0,len(flowerbed)):
            if flowerbed[i] == 1:
                self.updateSurroundingPlot(flowerbed,i)
        for i in range(0,len(flowerbed)):
            if flowerbed[i] == 0:
                n-=1
                self.updateSurroundingPlot(flowerbed,i)
            if n==0:
                return True
        return False

    def updateSurroundingPlot(self,flowerbed,index):
        if index == len(flowerbed)-1: #update left only
            flowerbed[index-1] = self.updateLeft(flowerbed, index)
        elif index == 0: #update right only
            flowerbed[index+1] = self.updateRight(flowerbed, index)
        else: #update both sides
            flowerbed[index-1] = self.updateLeft(flowerbed, index)
            flowerbed[index+1] = self.updateRight(flowerbed, index)

    
    def updateLeft(self,flowerbed,index):
        if flowerbed[index-1] != 1:
            flowerbed[index-1] = 2
    def updateRight(self,flowerbed,index):
        if flowerbed[index+1] != 1:
            flowerbed[index+1] = 2