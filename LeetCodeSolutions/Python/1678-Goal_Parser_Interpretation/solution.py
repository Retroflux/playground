# https://leetcode.com/problems/goal-parser-interpretation/submissions/916884213/

# Runtime: 27 ms, faster than 89.22% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 13.8 MB, less than 92.45% of Python3 online submissions for Goal Parser Interpretation.
#
# Problem:
#  You own a Goal Parser that can interpret a string command. The command consists of an 
#  alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret 
#  "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
#  The interpreted strings are then concatenated in the original order.
#  Given the string command, return the Goal Parser's interpretation of command.

#hello companies, yes I know about string interpretation, but 
# this is probably the least interesting file for you to look at. 
# Maybe try 0704 or 0589?
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("(al)","al").replace("()","o")