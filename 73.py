# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-06 01:39:51
# @Last Modified time: 2016-10-06 01:47:24
# @FileName: 73.py


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col = set()
        isSetRow = False
        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    isSetRow = True
                    col.add(i)
            if isSetRow:
                matrix[i] = map(lambda x: 0, matrix[i])
                isSetRow = False
        
        for i in col:
            for j in range(len(matrix)):
                matrix[j][i] = 0
