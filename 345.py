# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 00:10:36
# @Last Modified time: 2016-11-29 13:07:02
# @FileName: 345.py


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                vowels.append(i)
        # print(vowels_re)
        vowels_re = vowels[::-1]
        # print(vowels_re)
        news = []
        pos = 0
        for i in range(len(vowels)):
            # print(pos, vowels[i], vowels_re[i])
            news.append(s[pos:vowels[i]] + s[vowels_re[i]])
            pos = vowels[i] + 1
        news.append(s[pos:])
        return ''.join(news)

    # def reverseVowels(self, s):
    #     vowels = re.findall('(?i)[aeiou]', s)
    #     return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)