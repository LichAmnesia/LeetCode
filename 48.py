# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-04 09:10:46
# @Last Modified time: 2016-09-04 09:22:25
# @FileName: 48.py


# rotate the matrix 90
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        l -= 1
        for i in range(len(matrix) / 2):
            for j in range(len(matrix) / 2):
                t = matrix[i][j]
                matrix[i][j] = matrix[l - j][i]
                matrix[l - j][i] = matrix[l - i][l - j]
                matrix[l - i][l - j] = matrix[j][l - i]
                matrix[j][l - i] = t
