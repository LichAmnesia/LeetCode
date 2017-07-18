# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-26 20:46:53
# @Last Modified time: 2016-10-26 20:46:57
# @FileName: 42.py


class Solution(object):

    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        # write your code here
        left, right = 0, len(heights) - 1
        ans = 0
        block = 0
        cur = 0
        while left <= right:
            tmp = min(heights[left], heights[right])
            if tmp > cur:
                ans += (tmp - cur) * (right - left + 1)
                cur = tmp
            if heights[left] <= heights[right]:
                block += heights[left]
                left += 1
            else:
                block += heights[right]
                right -= 1
        return ans - block
