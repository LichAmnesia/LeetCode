# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-10 21:40:06
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-10 23:31:10


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        if len(path) < 1:
            return ""
        ans = []
        for s in path:
            if s == '':
                continue
            if s == '..':
                if len(ans) >= 1:
                    ans.pop()
            elif s != '.':
                ans.append(s)
        return '/' + '/'.join(ans)