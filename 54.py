# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-07 08:20:28
# @Last Modified time: 2016-09-07 10:49:21
# @FileName: 54.py


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []
        step = [len(matrix[0]), len(matrix) - 1]
        dirc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []
        now_dir = 0
        ir = 0
        ic = -1
        # print step
        while step[now_dir % 2] > 0:
            for i in range(step[now_dir % 2]):
                x, y = dirc[now_dir]
                ir += x
                ic += y
                # print ir, ic
                res.append(matrix[ir][ic])
            step[now_dir % 2] -= 1
            now_dir = (now_dir + 1) % 4
        return res
