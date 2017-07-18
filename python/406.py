# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-29 01:06:16
# @Last Modified time: 2016-09-29 01:53:11
# @FileName: 406.py


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        num = sorted(people)
        print num
        ans = [[] for x in range(len(num))]
        sum = [0 for x in range(len(num) + 1)]
        n = len(num)
        pre = -1
        tmp = []
        
        def update(pos, val):
            while pos <= n:
                sum[pos] += val
                pos += pos & -pos

        def getSum(pos):
            res = 0
            while pos > 0:
                res += sum[pos]
                pos -= pos & -pos
            return res

        def findKth(val):
            l = 1
            r = n
            while l <= r:
                mid = (l + r) >> 1
                if getSum(mid) < val:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        
        for i in range(len(num)):
            update(i + 1, 1)
        
        for i in range(len(num)):
            if num[i][0] != pre:
                for j in range(len(tmp)):
                    update(tmp[j], -1)
                tmp = []

            pos = findKth(num[i][1]+1)

            ans[pos - 1] = num[i]
            tmp.append(pos)
            
            pre = num[i][0]

        return ans
        
        