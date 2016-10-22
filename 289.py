# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-21 22:55:24
# @Last Modified time: 2016-10-21 22:55:32
# @FileName: 289.py


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        movx = [1, 1, 1, 0, 0, -1, -1, -1]
        movy = [1, 0, -1, 1, -1, 1, 0, -1]
        for x in range(len(board)):
            for y in range(len(board[0])):
                lives = 0
                for i in range(8):
                    dx = x + movx[i]
                    dy = y + movy[i]
                    if dx < 0 or dy < 0 or dx >= len(board) or dy >= len(board[0]):
                        continue
                    else:
                        lives += board[dx][dy] & 1
                if lives + (board[x][y] & 1) == 3 or lives == 3 or (board[x][y] == 0 and lives == 3):
                    board[x][y] |= 2
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] >>= 1
                        