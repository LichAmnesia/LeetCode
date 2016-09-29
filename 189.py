# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Date:   2016-09-25 11:45:04
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-09-25 12:03:57
# @Email: alwaysxiaop@gmail.com


class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        ans = []
        n = len(nums)
        nums[:k], nums[k:] = nums[n-k:], nums[:n-k]
        # nums[:] = nums[-k:] + nums[:len(nums)-k]
