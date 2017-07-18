# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-22 14:17:20
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-22 14:17:22
# @Email: shen.huang@colorado.edu

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return []
        if len(nums) == 1:
            return a * nums[0] * nums[0] + b * nums[0] + c
        ans = []
        if a == 0:
            
            for i in range(len(nums)):
                ans.append(b * nums[i] + c)
            i = 0
            while i < len(nums) - 1:
                if ans[i] > ans[i + 1]:
                    return ans[::-1]
                i += 1
            return ans
        elif a > 0:
            i, j = 0, len(nums) - 1
            while i <= j:
                if a * nums[i] * nums[i] + b * nums[i] + c >= a * nums[j] * nums[j] + b * nums[j] + c:
                    ans.append(a * nums[i] * nums[i] + b * nums[i] + c)
                    i += 1
                else:
                    ans.append(a * nums[j] * nums[j] + b * nums[j] + c)
                    j -= 1
            return ans[::-1]
        else:
            i, j = 0, len(nums) - 1
            while i <= j:
                if a * nums[i] * nums[i] + b * nums[i] + c <= a * nums[j] * nums[j] + b * nums[j] + c:
                    ans.append(a * nums[i] * nums[i] + b * nums[i] + c)
                    i += 1
                else:
                    ans.append(a * nums[j] * nums[j] + b * nums[j] + c)
                    j -= 1
            return ans
            