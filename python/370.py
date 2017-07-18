# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-19 12:48:47
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-19 12:49:32
# @Email: shen.huang@colorado.edu
# 在起点加上update值
# 在终点加1的位置减去update值
# 最后的求前缀和数组就是要的答案


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        nums = [0] * (length + 1)
        ans = []
        for i in range(len(updates)):
            a, b, c = updates[i]
            nums[a] += c
            nums[b + 1] += -c
        sum_of_nums = 0
        for i in range(length):
            sum_of_nums += nums[i]
            ans.append(sum_of_nums)
        return ans
