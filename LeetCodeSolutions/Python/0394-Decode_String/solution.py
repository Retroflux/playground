# https://leetcode.com/problems/sum-of-left-leaves/submissions/918252663/
# Date of Submission: 2023-03-19

# Runtime: 30 ms, faster than 73.89% of Python3 online submissions for Decode String.
# Memory Usage: 13.8 MB, less than 97.41% of Python3 online submissions for Decode String.
#
# Problem:

# Given an encoded string, return its decoded string.

# The encoding rule is : k[encoded_string], where the encoded_string inside 
# the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# Ex. encoded string: 3[a]2[bc]2[d3[ef2[g]]]
# Ex. decoded string: aaabcbcdefggefggefggdefggefggefgg


# You may assume that the input string is always valid;
# there are no extra white spaces, square brackets are well-formed, etc. 
# Furthermore, you may assume that the original data does not contain any 
# digits and that digits are only for those repeat numbers, k. 
# For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        outString = ""
        stringSegment = ""

        if s.isalpha():
            return s

        # add leading characters prior to first number onto stack
        while (len(s) > 0 and s[0].isnumeric() == False):
            outString = outString + s[0]
            s = s[1:]

        # process nested stacks
        while (len(s) > 0):
            if s[0].isnumeric() == True:  # append the number, remove the [
                stack.append(s.split("[", 1)[0])
                s = s.split("[", 1)[1]
                continue
            elif s[0] == "]":  # collapse the string segment
                tempString = ""
                # pop until stack is empty or a number is found
                while len(stack) > 0 and stack[-1].isnumeric() == False:
                    tempString = stack.pop() + tempString
                # if there's only one thing left on the stack (a number), output that
                # to the output string
                if len(stack) == 1:
                    stringSegment = tempString + stringSegment
                    outString = outString + (stringSegment * int(stack.pop()))
                    stringSegment = ""
                    tempString = ""
                else:  # still things on the stack to process, store partial answer on stack
                    stringSegment = (
                        tempString + stringSegment) * int(stack.pop())
                    stack.append(stringSegment)
                    stringSegment = ""
            else:  # is char in a string segment
                stack.append(s[0])
            s = s[1:]

        # clean up trailing characters left in stack
        while len(stack) > 0:
            stringSegment = stack.pop() + stringSegment
        outString = outString + stringSegment
        return outString
