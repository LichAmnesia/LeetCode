# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-05 00:08:29
# @Last Modified time: 2016-10-05 00:23:10
# @FileName: 49.py

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        dic = {}
        for i in range(len(strs)):
            k = 1
            for j in range(len(strs[i])):
                k *= prime[ord(strs[i][j]) - ord('a')]
            if k in dic:
                dic[k].append(strs[i])
            else:
                dic[k] = [strs[i]]
        ans = []
        for key in dic:
            ans.append([x for x in dic[key]])
        return ans