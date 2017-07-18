# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 00:37:59
# @Last Modified time: 2016-10-07 01:40:33
# @FileName: 79.py


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.row = len(board)
        if not self.row:
            return False
        self.col = len(board[0])
        self.visited = [[False for x in range(len(board[0]))] for y in range(len(board))]
        for i in range(self.row):
            for j in range(self.col):
                if self.visited[i][j] == False and word[0] == board[i][j]:
                    self.visited[i][j] = True
                    if self.dfs(board, i, j, 0, word):
                        return True
                    self.visited[i][j] = False
        return False

    def dfs(self, board, x, y, idx, word):
        if idx == len(word) - 1:
            return True
        direction = [[1, 0], [0, -1], [0, 1], [-1, 0]]
        for i in range(4):
            dx, dy = x + direction[i][0], y + direction[i][1]
            if dx >= 0 and dx < self.row and dy >= 0 and dy < self.col and self.visited[dx][dy] == False and word[idx + 1] == board[dx][dy]:
                self.visited[dx][dy] = True
                if self.dfs(board, dx, dy, idx + 1, word):
                    return True
                self.visited[dx][dy] = False
        return False