# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 18:19:35
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-02 18:31:33



class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_ = 0 
        l = 0
        r = len(height) - 1
        while l < r:
            max_ = max(max_, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                tmpl = height[l]
                while l < r and height[l] <= tmpl:
                    l += 1
            else:
                tmpr = height[r]
                while l < r and height[r] <= tmpr:
                    r -= 1
            # print l, r
        return max_