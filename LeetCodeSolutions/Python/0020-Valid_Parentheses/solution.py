# https://leetcode.com/submissions/detail/741402736/
# Date of Submission: 2022-07-07
# Updated: 2023-04-10

# Runtime: 24 ms, faster than 96.11% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.7 MB, less than 99.92% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:  # if odd
            return False

        if s.count("{") != s.count("}"):
            return False
        elif s.count("(") != s.count(")"):
            return False
        elif s.count("[") != s.count("]"):
            return False

        leftThings = ["{", "(", "["]
        currList = list()
        topOfList = ""

        for bracket in s:
            if bracket in leftThings:
                currList.append(bracket)  # add to list
            else:
                if (len(currList) == 0):
                    return False
                topOfList = currList[-1]
                if bracket == ")" and topOfList != "(":
                    return False
                elif bracket == "}" and topOfList != "{":
                    return False
                elif bracket == "]" and topOfList != "[":
                    return False
                else:
                    currList.pop()

        # if the while loop finishes && list is empty, then we have a balanced string
        if (len(currList) != 0):
            return False
        return True