# Problem: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        odd_freqs = []
        even_freqs = []
        for count in freq.values():
            if count % 2 == 0:
                even_freqs.append(count)
            else:
                odd_freqs.append(count)
        max_diff = None
        for odd in odd_freqs:
            for even in even_freqs:
                diff = odd - even
                if max_diff is None or diff > max_diff:
                    max_diff = diff
        if max_diff != None:
            return max_diff  
        else:
             -1
