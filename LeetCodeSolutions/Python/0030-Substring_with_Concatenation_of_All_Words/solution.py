import itertools

# this solution works, but exceeds the memory limit very quickly because of the algorithm's complexity
# A more memory-considerate solution would be to complete the problem without creating the permutation list and
# simply iterating through each string in words, looking for a match at (slidingWindowStarIndex + currStrLen), where
# currStrLen = the length of all pieces found so far. The pieces could be thrown into a stack, s.t. if you need to
# backtrack you can just remove the item from the stack and re-add it to the list (and clean up as required).
# This could be done recursively as well, but given the memory limit I don't think this is an option.
class Solution:
    def findSubstring(s: str, words: [str]) -> [int]:
        permutationStrings = [''.join(permutation) for permutation in list(itertools.permutations(words))]
        print(permutationStrings)
        return []
        # length of permutation string is greater than the string to search is an auto-fail
        if (len(permutationStrings[0]) > len(s)):
            return []
        slidingWindowSize = len(permutationStrings[0])
        returnList = []
        slidingWindowStartIndex = 0
        while (slidingWindowStartIndex + slidingWindowSize < len(s) + 1):
            if (s[slidingWindowStartIndex:slidingWindowStartIndex + slidingWindowSize] in permutationStrings):
                returnList.append(slidingWindowStartIndex)
            slidingWindowStartIndex += 1
        return returnList
