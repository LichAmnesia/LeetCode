# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-30 12:08:31
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-30 12:08:47


class Solution(object):

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = []
        i = 0
        ans = 0
        while i < len(heights):
            if len(stack) < 1 or heights[i] > heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                tmp = stack.pop()
                ans = max(
                    ans, heights[tmp] * (i if len(stack) < 1 else i - stack[-1] - 1))
        return ans
