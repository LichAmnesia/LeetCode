# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 00:25:24
# @Last Modified time: 2016-10-07 00:35:49
# @FileName: 139.py


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dic = {}

        def dfs(start):
            if start >= len(s):
                return True
            
            if start not in dic:
                for word in wordDict:
                    k = len(word)
                    for j in range(len(word)):
                        if start + j < len(s) and word[j] == s[start + j]:
                            k -= 1
                    if k == 0 and dfs(start + len(word)):
                        dic[start] = True
                        return dic[start]
                dic[start] = False
                return False
            return dic[start]
        
        # dfs(0)
        # print dic
        return dfs(0)