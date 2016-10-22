# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-21 22:53:05
# @Last Modified time: 2016-10-21 22:53:14
# @FileName: 417.py


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        if m * n == 0: return []
        topEdge = [(0, y) for y in range(n)]
        leftEdge = [(x, 0) for x in range(m)]
        pacific = set(topEdge + leftEdge)
        bottomEdge = [(m - 1, y) for y in range(n)]
        rightEdge = [(x, n - 1) for x in range(m)]
        atlantic = set(bottomEdge + rightEdge)
        
        def bfs(vset):
            queue = list(vset)
            dz = zip((1, 0, -1, 0), (0, 1, 0, -1))
            while len(queue) > 0:
                x, y = u = queue.pop(0)
                for nx, ny in dz:
                    dx, dy = x + nx, y + ny
                    if 0 <= dx < m and 0 <= dy < n:
                        if matrix[dx][dy] >= matrix[x][y]:
                            # queue.append()
                            if (dx, dy) not in vset:
                                queue.append((dx, dy))
                                vset.add((dx, dy))
            return vset
        
        pacSet = bfs(pacific)
        atlSet = bfs(atlantic)
        ans = pacSet & atlSet
        return map(list, ans)
            