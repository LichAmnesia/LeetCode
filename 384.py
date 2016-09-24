# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-23 20:43:34
# @Last Modified time: 2016-09-23 21:00:49
# @FileName: 384.py


class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = self.nums[:]
        random.shuffle(nums)
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
