# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 10:34:47
# @Last Modified time: 2016-11-17 10:36:54
# @FileName: 418.py
# http://bookshadow.com/weblog/2016/10/09/leetcode-sentence-screen-fitting/

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        wcount = len(sentence)
        wlen = map(len, sentence)
        slen = sum(wlen) + wcount
        dic = dict()
        pr = pc = pw = ans = 0
        while pr < rows:
            if (pc, pw) in dic:
                pr0, ans0 = dic[(pc, pw)]
                loop = (rows - pr0) / (pr - pr0 + 1)
                ans = ans0 + loop * (ans - ans0)
                pr = pr0 + loop * (pr -pr0)
            else:
                dic[(pc, pw)] = pr, ans
            scount = (cols - pc) / slen
            ans += scount
            pc += scount * slen + wlen[pw]
            if pc <= cols:
                pw += 1
                pc += 1
                if pw == wcount:
                    pw = 0
                    ans += 1
            if pc >= cols:
                pc = 0
                pr += 1
            # print pr, rows
        return ans 