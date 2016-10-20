# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 20:19:04
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-19 20:19:10


class Solution(object):

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        res = 0
        for y in range(len(board)):
            for x in range(len(board[0])):
                if all([board[y][x] == 'X',
                        not x or board[y][x - 1] != 'X',
                        not y or board[y - 1][x] != 'X']):
                    res += 1
        return res
