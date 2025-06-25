Problem: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        j = []
        res = []
        for i in range(len(nums)):
            if nums[i] == key:
                j.append(i)
        for i in range(len(nums)):
            for x in j:
                if abs(i - x) <= k:
                    res.append(i)
                    break
        return res
