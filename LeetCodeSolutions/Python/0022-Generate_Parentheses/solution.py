# https://leetcode.com/problems/generate-parentheses/submissions/930397198/
# Date of Submission: 2023-04-08

# Runtime: 33 ms, faster than 78.69% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.1 MB, less than 96.46% of Python3 online submissions for Generate Parentheses.

# Problem:


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        pList = ["("]
        newItems = []

        for i in range(1, n*2):
            for j in range(0, len(pList)):
                if len(pList[j]) == i:
                    if pList[j].count("(") > pList[j].count(")"):  # Add right bracket
                        newItems.append(deepcopy(pList[j]) + ")")
                    if pList[j].count("(") < n:  # Add left bracket
                        newItems.append(deepcopy(pList[j])+"(")
            pList = newItems
            newItems = []
        return pList
