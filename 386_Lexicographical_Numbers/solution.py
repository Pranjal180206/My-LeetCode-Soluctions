class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums = []
        for i in range(1, n+1):
            nums.append(i)
        num_str_sorted = sorted(map(str, nums))
        num_lex_sort = list(map(int, num_str_sorted))
        return num_lex_sort
