# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-30 01:45:57
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-30 01:46:03
# https://leetcode.com/problems/expression-add-operators/

class Solution(object):

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        def isLeadZeros(num):
            return num.startswith("00") or (int(num) and num.startswith("0"))

        def dfs(num, target, multiExp='', multiVal=1):
            ans = []
            if isLeadZeros(num):
                pass
            elif int(num) * multiVal == target:
                ans += num + multiExp,
            for x in range(len(num) - 1):
                lnum, rnum = num[:x + 1], num[x + 1:]
                if isLeadZeros(rnum):
                    continue
                right, rightVal = rnum + multiExp, int(rnum) * multiVal
                # op +
                for left in dfs(lnum, target - rightVal):
                    ans += left + '+' + right,
                # op -
                for left in dfs(lnum, target + rightVal):
                    ans += left + '-' + right,
                # op *
                for left in dfs(lnum, target, '*' + right, rightVal):
                    ans += left,
            return ans

        if not num:
            return []
        return dfs(num, target)
