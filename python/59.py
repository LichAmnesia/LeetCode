# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 11:45:25
# @Last Modified time: 2016-10-02 11:47:11
# @FileName: 59.py


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return [[]]
        step = [n, n - 1]
        dirc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        now_dir = 0
        ir = 0
        ic = -1
        itera = 1
        matrix = [[0 for i in range(n)] for j in range(n)]
        # print step
        while step[now_dir % 2] > 0:
            for i in range(step[now_dir % 2]):
                x, y = dirc[now_dir]
                ir += x
                ic += y
                # print ir, ic
                matrix[ir][ic] = itera
                itera += 1
            step[now_dir % 2] -= 1
            now_dir = (now_dir + 1) % 4
        return matrix