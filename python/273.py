# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-30 00:25:00
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-30 00:25:07


class Solution(object):

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        lv1 = "Zero One Two Three Four Five Six Seven Eight Nine Ten \
               Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        lv2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        lv3 = "Hundred"
        lv4 = "Thousand Million Billion".split()
        ans = []
        lv4_num = 0
        while num:
            word = ''
            digit, num = num % 1000, num / 1000
            if digit > 99:
                word += lv1[digit / 100] + ' ' + lv3 + ' '
                digit %= 100
            if digit > 19:
                word += lv2[digit / 10 - 2] + ' '
                digit %= 10
            if digit > 0:
                word += lv1[digit] + ' '
            word = word.strip()
            if word:
                word += ' ' + lv4[lv4_num - 1] if lv4_num else ''
                ans += word,
            lv4_num += 1
        return ' '.join(ans[::-1]) if ans else "Zero"
