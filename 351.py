# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-18 10:26:35
# @Last Modified time: 2016-11-18 11:50:49
# @FileName: 351.py

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def dfs(num, len_):
            if len_ > n: return 0
            res = 0
            if len_ >= m: res += 1
            vis[num] = True
            for i in range(1, 10):
                if not vis[i] and (jumps[num][i] == 0 or vis[jumps[num][i]]):
                    # print num, i, len_ + 1, res
                    res += dfs(i, len_ + 1)
                    # print num, i, len_ + 1, res
            vis[num] = False
            return res
        
        jumps = [[0] * 10 for x in range(10)]
        jumps[1][3] = jumps[3][1] = 2
        jumps[4][6] = jumps[6][4] = 5
        jumps[7][9] = jumps[9][7] = 8
        jumps[1][7] = jumps[7][1] = 4
        jumps[2][8] = jumps[8][2] = 5
        jumps[3][9] = jumps[9][3] = 6
        jumps[1][9] = jumps[9][1] = jumps[3][7] = jumps[7][3] = 5
        vis = [False] * 10
        
        ans = dfs(1, 1) * 4
        # print ans
        ans += dfs(2, 1) * 4
        # print ans
        ans += dfs(5, 1)
        # print ans
        return ans
        