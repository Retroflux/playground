# https://leetcode.com/submissions/detail/719216479/
# Date of Submission: 2022-06-10

# Runtime: 32 ms, faster than 94.56% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14 MB, less than 48.73% of Python3 online submissions for Longest Common Prefix.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #constraints:
        #   1 <= strs.length <= 200
        #   0 <= strs[i].length <= 200
        #   strs[i] consists of only lower-case English letters.
        
        if(len(strs) == 1):
            return strs[0]
        
        minLength = len(strs[0])
        
        #find the shortest string
        for string in strs:
            if(len(string) < minLength):
                minLength = len(string)
        
        #empty string in list
        if(minLength == 0):
            return ""
        
        #iterate through all strings until no match found
        for i in range(0,minLength):
            charMatch = strs[0][i]
            for string in strs:
                if(string[i] != charMatch):
                    return strs[0][:i]
        return strs[0][:minLength]