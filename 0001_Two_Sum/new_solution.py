class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevNums = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevNums:
                return [prevNums[diff], i]
            prevNums[num] = i
