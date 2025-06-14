# Problem: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit

class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = '0123456789'
        str_num = str(num)
        max_val = num
        min_val = num
        for i in digits:
            for j in digits:
                if i == j:
                    pass
                new_str_num = str_num.replace(i ,j)
                new_num = int(new_str_num)
                max_val = max(max_val, new_num)
                min_val = min(min_val, new_num)
        return max_val - min_val
