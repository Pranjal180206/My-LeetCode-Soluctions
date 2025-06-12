class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff = []
        for i in range(len(nums)):
            curr = nums[i]
            next = nums[(i+1) % len(nums)]
            diff.append(abs(curr - next))
        return max(diff)
