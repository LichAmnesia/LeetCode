# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-18 23:33:14
# @Last Modified time: 2016-10-18 23:55:16
# @FileName: 166.py


class Solution(object):

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)

        reslist = []
        resdic = {}
        loop_str = ''
        if numerator == 0:
            return '0'
        while numerator:
            reslist.append(str(numerator / denominator))
            print numerator
            numerator = 10 * (numerator % denominator)
            remain_pos = resdic.get(numerator)
            # print remain_pos, reslist
            if remain_pos is not None:
                loop_str = ''.join(reslist[remain_pos + 1:])
                reslist = reslist[: - len(loop_str)]
                break
            resdic[numerator] = len(reslist) - 1
        ans = reslist[0]
        if len(reslist) > 1 or len(loop_str) >= 1:
            ans += '.'
        if len(loop_str) >= 1:
            ans += ''.join(reslist[1:]) + '(' + loop_str + ')'
        else:
            ans += ''.join(reslist[1:])
        if sign:
            ans = '-' + ans
        return ans
        # print reslist, loop_str
