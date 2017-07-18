# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 11:16:56
# @Last Modified time: 2016-10-02 11:22:36
# @FileName: 240.py
# http://bookshadow.com/weblog/2015/07/23/leetcode-search-2d-matrix-ii/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        j = len(matrix[0]) - 1
        for i in range(len(matrix)):
            while j > 0 and matrix[i][j] > target:
                j -= 1
            if matrix[i][j] == target:
                return True
        return False