# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2017-01-01 12:55:13
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2017-01-01 12:55:16
# @Email: shen.huang@colorado.edu

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:-1}
        sum = 0
        max_len = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum not in dic:
                dic[sum] = i
            if sum - k in dic:
                max_len = max(max_len, i - dic[sum - k])
        return max_len