# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 15:43:25
# @Last Modified time: 2016-09-20 19:44:51
# @FileName: 223.py


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if sorted([A, E, C, G])[1] >= A and sorted([A, E, C, G])[2] <= C and sorted([B, D, F, H])[1] >= B and sorted([B, D, F, H])[2] <= D:
            return (D - B) * (C - A) + (H - F) * (G - E) - (sorted([A, E, C, G])[2] - sorted([A, E, C, G])[1]) * (sorted([B, D, F, H])[2] - sorted([B, D, F, H])[1])
        return (D - B) * (C - A) + (H - F) * (G - E)
