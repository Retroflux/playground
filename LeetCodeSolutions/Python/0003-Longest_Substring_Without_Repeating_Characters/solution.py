
# https://leetcode.com/submissions/detail/718127460/
# Date of Submission: 2022-06-09

# Runtime: 60 ms, faster than 92% of Python online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 50.72% of Python online submissions for Longest Substring Without Repeating Characters.

#NOTE: This could likely be made to have less memory usage if the substring was managed in-place with the given string; however,
#       this change would likely increase the runtime because of the constant spliced substring lookups. Memory down, runtime up.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        currentList = []
        maxLength = 0
        
        for i in range(0,len(s)):
            if (s[i] in currentList):
                while(currentList.pop(0) != s[i]):
                    continue
            currentList.append(s[i])
            if (maxLength < len(currentList)):
                maxLength = len(currentList)
        
        return maxLength