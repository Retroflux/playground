# https://leetcode.com/problems/backspace-string-compare/submissions/920889676/
# Date of Submission: 2023-03-23

# Runtime: 29 ms, faster than 84.11% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 14 MB, less than 85.20% of Python3 online submissions for Backspace String Compare.
#
# Problem:
#  Given two strings s and t, return true if they are equal when both are typed into empty text
#  editors. '#' means a backspace character.
#  Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.createEditorOutput(s) == self.createEditorOutput(t)

    def createEditorOutput(self, userInput):
        outString = list()
        if "#" not in userInput:
            return userInput

        for char in userInput:
            if char == "#":
                if len(outString) == 0:
                    continue
                else:
                    outString = outString[:-1]
            else:
                outString.append(char)
        return "".join(outString)
