# Problem: https://leetcode.com/problems/valid-word/

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        vowels = False
        consonants = False
        for ch in word:
            if ch.isalpha():
                if ch.lower() in 'aeiou':
                    vowels = True
                else:
                    consonants = True
            if vowels and consonants:
                return True
        return vowels and consonants
