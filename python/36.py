# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-04 23:21:37
# @Last Modified time: 2016-10-04 23:33:36
# @FileName: 36.py


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            se = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in se or board[i][j] > '9' or board[i][j] < '1':
                    return False
                elif board[i][j] not in se:
                    se.add(board[i][j])

        for j in range(len(board[0])):
            se = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in se or board[i][j] > '9' or board[i][j] < '1':
                    return False
                elif board[i][j] not in se:
                    se.add(board[i][j])

        for xi in range(0, len(board), 3):
            for xj in range(0, len(board[0]), 3):
                se = set()
                for i in range(xi, xi + 3):
                    for j in range(xj, xj + 3):
                        if board[i][j] == '.':
                            continue
                        elif board[i][j] in se or board[i][j] > '9' or board[i][j] < '1':
                            return False
                        elif board[i][j] not in se:
                            se.add(board[i][j])
        return True