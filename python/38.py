# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-04 23:19:16
# @Last Modified time: 2016-10-04 23:37:37
# @FileName: 38.py


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for xn in range(n):
            num = 1
            ans = []
            for i in range(len(s)):
                if i < len(s) - 1 and s[i] == s[i + 1]:
                    num += 1
                else:
                    ans.append(str(num) + s[i])
            s = ''.join(ans)
        return s
