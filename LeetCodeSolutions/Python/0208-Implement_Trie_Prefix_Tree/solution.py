# https://leetcode.com/problems/implement-trie-prefix-tree/submissions/916993890/
# Date of Submission: 2023-03-17

# Runtime: 156 ms, faster than 85.87% of Python3 online submissions for Implement Trie Prefix Tree.
# Memory Usage: 31.8 MB, less than 25.40% of Python3 online submissions for Implement Trie Prefix Tree.
#
# Problem:

# A trie(pronounced as "try") or prefix tree is a tree data structure used to 
# efficiently store and retrieve keys in a dataset of strings. There are various 
# applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie(i.e., was 
#   inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string 
#   word that has the prefix prefix, and false otherwise.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()  # top of Trie

    def insert(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.is_word = True

    def search(self, word: str) -> bool:
        root = self.root
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.is_word

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for char in prefix:
            if char not in root.children:
                return False
            root = root.children[char]
        return True
