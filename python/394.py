# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 19:56:19
# @Last Modified time: 2016-10-01 20:28:27
# @FileName: 394.py


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # stack = []
        # res = ''
        # for i in range(len(s)):
        #     if s[i] != ']':
        #         stack.append(s[i])
        #     else:
        #         tmp = stack.pop()
        #         ans = ''
        #         while tmp != '[':
        #             ans = tmp + ans
        #             tmp = stack.pop()
        #         tmp = stack[-1]
        #         num = ''
        #         while tmp.isdigit():
        #             stack.pop()
        #             num = tmp + num
        #             if len(stack) >= 1:
        #                 tmp = stack[-1]
        #             else:
        #                 break
        #         num = int(num)
        #         ans1 = ''
        #         for j in range(num):
        #             ans1 = ans1 + ans
        #         stack.append(ans1)
        # return ''.join(stack)
        while '[' in s:
            s = re.sub('(\d+)\[([a-z]*)\]', lambda m: m.group(1) * m.group(2), s)
        return s