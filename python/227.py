# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 20:24:36
# @Last Modified time: 2016-10-07 20:51:59
# @FileName: 227.py


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = re.sub(r'\d+', ' \g<0> ', s)
        op = {'+': operator.add, '-': operator.sub,
              '*': operator.mul, '/': operator.floordiv}
        s = s.split()
        total = idx = now = 0
        func = op['+']
        while idx < len(s):
            if s[idx] in '+-':
                total = func(total, now)
                func = op[s[idx]]
            elif s[idx] in '*/':
                now = op[s[idx]](now, int(s[idx + 1]))
                idx += 1
            else:
                now = int(s[idx])
            idx += 1
        return func(total, now)
