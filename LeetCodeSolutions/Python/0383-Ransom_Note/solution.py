# https://leetcode.com/problems/linked-list-random-node/submissions/https://leetcode.com/problems/ransom-note/submissions/912769096/
# Date of Submission: 2023-03-10

# Runtime: 39 ms, faster than 93% of Python3 online submissions for Ransom Note.
# Memory Usage: 14 MB, less than 99.79% of Python3 online submissions for Ransom Note.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for letter in ransomNote:
            if magazine.find(letter) == -1:
                return False
            magazine = magazine.replace(
                magazine[magazine.find(letter)], "", 1)

        return True
