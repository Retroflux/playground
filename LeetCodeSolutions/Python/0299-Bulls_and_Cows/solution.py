# https://leetcode.com/problems/bulls-and-cows/submissions/920154081/
# Date of Submission: 2023-03-22

# Runtime: 54 ms, faster than 20.63% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 13.7 MB, less than 98.8% of Python3 online submissions for Bulls and Cows.
#
# Problem:

#  You write down a secret number and ask your friend to guess what the number is .
#  When your friend makes a guess, you provide a hint with the following info:

#    The number of "bulls", which are digits in the guess that are in the correct position.
#    The number of "cows", which are digits in the guess that are in your secret number but
#    are located in the wrong position. Specifically, the non-bull digits in the guess that 
#    could be rearranged such that they become bulls.
#    
#  Given the secret number secret and your friend's guess guess, 
#  return the hint for your friend's guess.


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        guess_dict = {}
        secret_dict = {}
        for i in range(0, len(secret)):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                if secret[i] in guess_dict and guess_dict[secret[i]] > 0:
                    cows += 1
                    guess_dict[secret[i]] -= 1
                else:
                    secret_dict[secret[i]] = secret_dict.get(secret[i], 0) + 1
                if guess[i] in secret_dict and secret_dict[guess[i]] > 0:
                    cows += 1
                    secret_dict[guess[i]] -= 1
                else:
                    guess_dict[guess[i]] = guess_dict.get(guess[i], 0) + 1

        return str(bulls)+"A"+str(cows)+"B"
