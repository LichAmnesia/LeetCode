# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 11:54:21
# @Last Modified time: 2016-11-17 11:54:25
# @FileName: 388.py


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        s = input.split('\n')
        ans = lengthS = 0
        stack = [(-1, 0)]
        for line in s:
            depth = line.count('\t')
            name = line.replace('\t', '')
            topDepth, topLength = stack[-1]
            while depth <= topDepth:
                stack.pop()
                lengthS -= topLength
                topDepth, topLength = stack[-1]
            length = len(name) + (depth > 0)
            lengthS += length
            stack.append((depth, length))
            if name.count('.'):
                ans = max(ans, lengthS)
        return ans