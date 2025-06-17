# Problem: https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        palindrome = False
        str_x = str(x)
        if X < 0:
            return palindrome
        if str_x == str_x[::-1]:
            palindrome = True
        return palindrome
