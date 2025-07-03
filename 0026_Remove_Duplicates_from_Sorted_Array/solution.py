# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
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
        res = list(freq.keys())
        res.sort()
        for i in range(len(nums)):
            if i < len(res):
                nums[i] = res[i]
        return len(res)
