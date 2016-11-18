# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 17:17:20
# @Last Modified time: 2016-11-17 17:17:21
# @FileName: 266.py

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = collections.Counter(s)
        cnt = 0
        for i in dic:
            if dic[i] % 2 == 0:
                continue
            else:
                cnt += 1
                if cnt >= 2:
                    return False
        return True