# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-03 23:38:45
# @Last Modified time: 2016-09-03 23:50:12
# @FileName: 378.py


# Solution: change matrix to list, then apply sort function
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        num = []
        for i in range(n):
            num.extend(matrix[i])
        num = sorted(num)
        # print num
        k -= 1
        return num[k]

matrix = [ 
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
res = Solution()
print res.kthSmallest(matrix, k)
