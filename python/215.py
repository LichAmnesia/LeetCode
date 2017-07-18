# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 18:36:05
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-02 18:42:15


import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums1 = []
        nums2 = []
        val = random.choice(nums)
        for i in range(len(nums)):
            if nums[i] < val:
                nums1.append(nums[i])
            elif nums[i] > val:
                nums2.append(nums[i])
        if k <= len(nums2):
            return self.findKthLargest(nums2, k)
        if k > len(nums) - len(nums1):
            return self.findKthLargest(nums1, k - (len(nums) - len(nums1)))

        return val
