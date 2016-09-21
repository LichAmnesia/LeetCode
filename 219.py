# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 14:53:18
# @Last Modified time: 2016-09-20 14:55:27
# @FileName: 219.py


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = i
            else:
                if i - m[nums[i]] <= k:
                    return True
                m[nums[i]] = i
        return False
