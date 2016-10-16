# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-15 23:19:37
# @Last Modified time: 2016-10-15 23:51:31
# @FileName: 332.py


class Solution(object):

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        tickets = sorted(tickets)
        dic = collections.defaultdict(list)

        for i, j in tickets[::-1]:
            dic[i] += j,
        router = []
        u = 'JFK'

        def dfs(u):
            while dic[u]:
                dfs(dic[u].pop())

            router.append(u)
        dfs(u)
        return router[::-1]
