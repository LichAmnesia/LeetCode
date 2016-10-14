# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-14 15:37:21
# @Last Modified time: 2016-10-14 15:49:12
# @FileName: 133.py

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneGraph(self, node):
        def dfs(node, dic):
            if not node:
                return None
            if node not in dic:
                dic[node] = UndirectedGraphNode(node.label)
                dic[node].neighbors = [dfs(i, dic) for i in node.neighbors]
            return dic[node]
        return dfs(node, {})
