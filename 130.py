# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 00:28:29
# @Last Modified time: 2016-10-19 00:30:26
# @FileName: 130.py



class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n < 1:
            return 
        m = len(board[0])
        
        def bfs(x, y):
            dic = [[1, 0], [0, 1], [-1, 0] ,[0, -1]]
            queue = [(x, y)]
            board[x][y] = 'A'
            while queue:
                x, y = queue.pop(0)
                for i in range(4):
                    dx = x + dic[i][0]
                    dy = y + dic[i][1]
                    if dx >= 0 and dy >= 0 and dx < n and dy < m and board[dx][dy] == 'O':
                        board[dx][dy] = 'A'
                        queue.append((dx, dy))
                    
            
        for i in range(n):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][m - 1] == 'O':
                bfs(i, m - 1)
            
        for j in range(m):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[n - 1][j] == 'O':
                bfs(n - 1, j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'