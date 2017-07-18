# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 00:00:25
# @Last Modified time: 2016-10-07 00:13:29
# @FileName: 17.py


class Solution(object):
    memo = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        ans = []

        def dfs(idx, path):
            if len(path) == len(digits):
                ans.append(path)
                return
            for i in self.memo[digits[idx]]:
                dfs(idx + 1, path + i)

        dfs(0, '')
        return ans
