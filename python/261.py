# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-10 21:57:40
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-11-10 21:59:03




class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        e = set([])
        for i in range(n):
            a, b = edges[i][0], edges[i][1]
            print "s", a, b
            if a in e and b in e:
                return False
            else:
                e.add(a)
                e.add(b)
        return True

res = Solution()
edges = [[0,1],[0,2],[1,2],[2,3],[2,4]]
res.validTree(5, edges)