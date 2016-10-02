# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 20:28:30
# @Last Modified time: 2016-10-01 21:59:09
# @FileName: 313.py
# 记住一个数组，记录每次ugly number是从哪里来的。仔细观察上述三个列表，我们可以发现每个子列表都是一个丑陋数分别乘以2,3,5，
# 而要求的丑陋数就是从已经生成的序列中取出来的，我们每次都从三个列表中取出当前最小的那个加入序列，请参见代码如下：


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        num_of_list = [0 for x in range(len(primes))]
        for i in range(n):
            min_num = min([res[num_of_list[x]] * primes[x] for x in range(len(num_of_list))])
            for j in range(len(primes)):
                if min_num == primes[j] * res[num_of_list[j]]:
                    num_of_list[j] += 1
            res.append(min_num)
        print res
        return res[n - 1]