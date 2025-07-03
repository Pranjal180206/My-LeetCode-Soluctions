class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        reverse_num = 0
        while num > 0:
            last_digit = num % 10
            num = num // 10
            reverse_num = last_digit + reverse_num*10
        if reverse_num == x:
            return True
        else:
            return False
