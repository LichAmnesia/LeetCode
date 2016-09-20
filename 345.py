# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 00:10:36
# @Last Modified time: 2016-09-20 00:42:31
# @FileName: 345.py


class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                res.append(i)
        revese = res[::-1]
        t = ''
        now = 0
        for i in range(len(res)):
            t += s[now:res[i]] + s[revese[i]]
            now = res[i] + 1
        t += s[now:]
        return t

    # def reverseVowels(self, s):
    #     vowels = re.findall('(?i)[aeiou]', s)
    #     return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)