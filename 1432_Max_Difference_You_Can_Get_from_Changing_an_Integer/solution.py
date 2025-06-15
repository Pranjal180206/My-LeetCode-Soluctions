# Problem: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/ 

class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = '0123456789'
        str_num = str(num)
        a = num
        b = num
        for i in digits:
            for j in digits:
                if i == j:
                    pass
                new_str_num = str_num.replace(i ,j)
                if new_str_num[0] == '0' or int(new_str_num) == 0:
                    continue
                new_num = int(new_str_num)
                a = max(a, new_num)
                b = min(b, new_num)
        return a - b
