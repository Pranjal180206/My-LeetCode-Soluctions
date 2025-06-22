# Problem: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        res = []
        group = []
        for i in range(0, len(s), k):
            group = s[i:i+k]
            if len(group) < k:
                group = group + fill * (k - len(group))
            res.append(group)
        return res
                
