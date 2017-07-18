# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-18 22:28:03
# @Last Modified time: 2016-10-18 22:38:04
# @FileName: 151.py


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = [x for x in s.split(' ')[::-1] if len(x) > 0]
        # print len(s),s
        if len(s) < 1:
            return ''
        return ' '.join(s)


ans = Solution()
print ans.reverseWords(' ')