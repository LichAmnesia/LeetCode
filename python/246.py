# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 17:08:06
# @Last Modified time: 2016-11-17 17:08:07
# @FileName: 246.py

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'8':'8', '6':'9', '1':'1', '9':'6', '0':'0'}
        
        for i in num:
            if i not in dic:
                return False
        rnum = map(str, num[::-1])
        print rnum
        for i in range(len(rnum)):
            rnum[i] = dic[rnum[i]]
        rnum = ''.join(rnum)
        return rnum == num
        