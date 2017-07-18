# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-04 23:50:13
# @Last Modified time: 2016-10-05 00:08:23
# @FileName: 241.py


class Solution(object):

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        def dfs(input):
            res = []
            for i in range(len(input)):
                if input[i] == '-' or input[i] == '+' or input[i] == '*':
                    A = dfs(input[0:i])
                    B = dfs(input[i + 1:])
                    for j in range(len(A)):
                        for k in range(len(B)):
                            if input[i] == '-':
                                res.append(A[j] - B[k])
                            elif input[i] == '+':
                                res.append(A[j] + B[k])
                            elif input[i] == '*':
                                res.append(A[j] * B[k])
            if len(res) < 1:
                return int(input)
            return res

        return dfs(input)