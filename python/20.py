# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 15:04:23
# @Last Modified time: 2016-09-20 15:13:40
# @FileName: 20.py


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for i in s:
            if i in ['(', '[', '{']:
                st.append(i)
            else:
                if len(st) < 1:
                    return False
                if i == ')':
                    if st[-1] == '(':
                        st.pop()
                    else:
                        return False
                if i == ']':
                    if st[-1] == '[':
                        st.pop()
                    else:
                        return False
                if i == '}':
                    if st[-1] == '{':
                        st.pop()
                    else:
                        return False
        if len(st) < 1:
            return True
        return False


