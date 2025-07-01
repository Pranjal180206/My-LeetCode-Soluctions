# Problem: https://leetcode.com/problems/find-the-original-typed-string-i/

class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        res = 0
        freq = {}
        for i in range(len(word) - 1):
            if word[i] == word[i+1]:
                if word[i] in freq:
                    freq[word[i]] += 1
                else:
                    freq[word[i]] = 1
        for i in freq:
            res += freq[i]   
        return res + 1
