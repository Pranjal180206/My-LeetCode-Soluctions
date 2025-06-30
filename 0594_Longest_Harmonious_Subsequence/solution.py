# Problem: https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        max_len = 0
        for i in freq:
            if i+1 in freq:
                curr_len = freq[i] + freq[i+1]
                if curr_len > max_len:
                    max_len = curr_len
        return max_len
