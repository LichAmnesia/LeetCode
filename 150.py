# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-11 16:35:00
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-11 16:44:05


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in '-+/*':
                a = stack.pop()
                b = stack.pop()
                a, b = b, a
                if token == '-':
                    stack.append(a - b)
                elif token == '+':
                    stack.append(a + b)
                elif token == '/':
                    stack.append(int(operator.truediv(a, b)))
                elif token == '*':
                    stack.append(a * b)
                # print stack[-1
            else:
                stack.append(int(token)
        return stack[0]