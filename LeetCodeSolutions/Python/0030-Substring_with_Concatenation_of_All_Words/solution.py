class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        pass
        # TODO create a permutation list of all possible strings using all four words
            # TODO ex. three strings would be [a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a]
        # TODO use a sliding window of size equal to the permutations to check substrings from left to right
        # TODO Immediately output [] if the size of the sliding window is greater than len(s)
        # TODO "if slidingWindowSubstring in permutationWordList: outputList.append(slidingWindowSubstringStartIndex)"
        # TODO return outputList
