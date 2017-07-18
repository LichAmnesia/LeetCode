# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-22 17:46:43
# @Last Modified time: 2016-09-22 18:03:22
# @FileName: 299.py


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        ball = 0
        cows = 0
        se = {}
        gu = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                ball += 1
            if secret[i] not in se:
                se[secret[i]] = 1
            else:
                se[secret[i]] += 1
            if guess[i] not in gu:
                gu[guess[i]] = 1
            else:
                gu[guess[i]] += 1
        for key in gu:
            if key in se:
                tmp = se[key]
            else:
                tmp = 0
            cows += min(gu[key], tmp)
        return str(ball) + 'A' + str(cows - ball) + 'B'
