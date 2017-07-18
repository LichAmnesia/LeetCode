# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-21 22:53:28
# @Last Modified time: 2016-10-21 22:53:48
# @FileName: 310.py


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0:
            return []
        elif len(edges) == 0:
            return [0]

        graph = {}

        for (x, y) in edges:
            if x in graph:
                graph[x].append(y)
            else:
                graph[x] = [y]

            if y in graph:
                graph[y].append(x)
            else:
                graph[y] = [x]
                
        def bfs(src):
            vis = [0] * n
            max_dep = 0
            ans_u = 0
            queue = [(src, 0)]
            vis[src] = True
            path = [src]
            while len(queue) > 0:
                u, l = queue.pop(0)
                if l > max_dep:
                    max_dep = l
                    ans_u = u
                    path.append(u)
                for i in graph[u]:
                    if not vis[i]:
                        queue.append((i, l + 1))
                        vis[i] = True       
            return ans_u, max_dep, path
            
            
        u, dep, path = bfs(0)
        u, dep, path = bfs(u)
        print dep
        if dep % 2:
            return path[dep / 2: dep / 2 + 2]
        return path[dep / 2: dep / 2 + 1]