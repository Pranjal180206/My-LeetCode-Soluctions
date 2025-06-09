# Problem: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# Initial soluction
# Memory Limit Exceeded

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nums = [] 
        for i in range(1, n+1):
            nums.append(i)
        nums_str_sorted = sorted(map(str, nums))
        nums_lex_sort = list(map(int, nums_str_sorted))
        return nums_lex_sort[k-1]
