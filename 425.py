# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 11:54:00
# @Last Modified time: 2016-11-17 11:54:01
# @FileName: 425.py


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        n = len(words)
        m = len(words[0]) if n else 0
        mdict = collections.defaultdict(set)
        for word in words:
            for i in range(m):
                mdict[word[:i]].add(word)
            
        
        matrix = []
        ans = []
        
        def dfs(word, row):
            matrix.append(word)
            if row == m:
                ans.append(matrix[:])
            else:
                prefix = ''.join(matrix[i][row] for i in range(row))
                for w in mdict[prefix]:
                    dfs(w, row + 1)
            matrix.pop()
        
        for word in words:
            dfs(word, 1)
        return ans