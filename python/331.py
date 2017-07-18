# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-06 16:52:36
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-06 17:10:47


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        pre = preorder.split(',')
        for item in pre:
            stack.append(item)
            
            while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
                
        if len(stack) == 1 and stack[0] == '#':
            return True
        return False