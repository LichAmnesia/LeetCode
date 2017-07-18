# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-18 16:36:18
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-18 16:36:20
# @Email: shen.huang@colorado.edu


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        if n < 1: return 0
        r = sum(nums)
        l = r / n
        while l <= r:
            mid = (l + r) / 2
            valid = True
            cnt = 0
            need = m
            for i in range(len(nums)):
                if nums[i] > mid:
                    valid = False
                    break
                elif cnt + nums[i] > mid:
                    need -= 1
                    cnt = nums[i]
                else:
                    cnt += nums[i]
                
                if need == 0:
                    valid = False
                    break
            if valid:
                r = mid - 1
            else:
                l = mid + 1
        # the first bigger than
        return l
            