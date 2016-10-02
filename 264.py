# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 21:44:09
# @Last Modified time: 2016-10-01 21:54:17
# @FileName: 264.py
# 记住一个数组，记录每次ugly number是从哪里来的。仔细观察上述三个列表，我们可以发现每个子列表都是一个丑陋数分别乘以2,3,5，
# 而要求的丑陋数就是从已经生成的序列中取出来的，我们每次都从三个列表中取出当前最小的那个加入序列，请参见代码如下：


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [2, 3, 5]
        res = [1]
        num_of_list = [1, 1, 1]
        for i in range(n):
            min_num = min([num_of_list[x] * nums[x] for x in range(len(num_of_list))])
            for j in range(len(nums)):
                if min_num == nums[j] * num_of_list[j]:
                    num_of_list[j] += 1
            res.append(min_num)
        return res[n - 1]