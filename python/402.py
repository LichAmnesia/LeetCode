# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-14 16:25:22
# @Last Modified time: 2016-10-14 16:25:27
# @FileName: 402.py


class Solution(object):

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        delete_number = 0
        num_list = [int(i) for i in num]
        num = num_list
        stack = [0]
        for i in range(len(num)):
            while stack[-1] > num[i] and delete_number < k:
                stack.pop()
                delete_number += 1
            stack.append(num[i])

        while delete_number < k:
            stack.pop()
            delete_number += 1
        while len(stack) > 1 and stack[0] == 0:
            del stack[0]
        if len(stack) < 1:
            return "0"

        return ''.join([str(x) for x in stack])
