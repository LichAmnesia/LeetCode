# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-30 12:21:31
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-30 12:21:34


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

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n < 1:
            return 0
        m = len(matrix[0])
        heights = [[0] * m for x in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    heights[i][j] = 0
                else:
                    heights[i][j] = heights[i - 1][j] + 1 if i != 0 else 1

        ans = 0
        for i in range(n):
            ans = max(ans, self.largestRectangleArea(heights[i]))
        return ans
