# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 17:48:15
# @Last Modified time: 2016-09-18 18:08:24
# @FileName: 401.py


class Solution(object):
    def readBinaryWatch(self, num):
        """f        :type num: int
        :rtype: List[str]
        """
        self.val = [1, 2, 4, 8, 16, 32, 100, 200, 400, 800]
        self.res = []
        vis = [0 for x in range(len(self.val))]
        self.dfs(num, 0, vis, 0)
        return self.res

    def dfs(self, remain, now, vis, id):
        if remain == 0:
            minu = now % 100
            hour = now / 100
            if hour > 11:
                return
            if minu > 59:
                return
            if minu < 10:
                minu = '0' + str(minu)
            else:
                minu = str(minu)
            self.res.append(str(hour) + ':' + minu)
            return

        for i in range(id, len(self.val)):
            if vis[i] == 0:
                vis[i] = 1
                self.dfs(remain - 1, now + self.val[i], vis, i + 1)
                vis[i] = 0
        return