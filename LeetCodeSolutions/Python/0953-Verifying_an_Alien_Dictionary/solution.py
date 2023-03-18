# https://leetcode.com/problems/verifying-an-alien-dictionary/submissions/917659164

# Runtime: 40 ms, faster than 49.68% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 13.7 MB, less than 99.2% of Python3 online submissions  for Verifying an Alien Dictionary.
#
# Problem:
#  In an alien language, surprisingly, they also use English lowercase letters, 
#  but possibly in a different order. The order of the alphabet is some 
#  permutation of lowercase letters.

#  Given a sequence of words written in the alien language, 
#  and the order of the alphabet, return true if and only if the given 
#  words are sorted lexicographically in this alien language.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for firstWord in words[:-1]:
            for secondWord in words[1:]:
                totalMatch = 1
                for i in range(0, min(len(firstWord), len(secondWord))):
                    #move to next character if they're the same (ex. apple & apples)
                    if order.find(firstWord[i]) == order.find(secondWord[i]):
                        continue
                    #if alien 'A' comes after alien 'B', it's not sorted, return False
                    elif order.find(firstWord[i]) > order.find(secondWord[i]):
                        return False
                    #break out on first comparison that yields a true statement
                    else:
                        totalMatch = 0
                        break
                #edge case for things like fw: apples, sw: apple; this should return false
                if totalMatch == 1 and len(secondWord) < len(firstWord):
                    return False
        #if all is gucci, return true
        return True
