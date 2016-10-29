# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-28 15:37:37
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-28 15:37:45


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        sysmax = 100000000.0
        ans = 0
        for i in range(len(points)):
            dic = {}
            dup = 1
            dic[sys.maxint] = 0
            for j in range(len(points)):
                if i == j:
                    continue
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    dup += 1
                    continue
                # key = 1 if 1 else 0
                key = (sysmax if (points[j].x - points[i].x) == 0 else 1.0 *
                       (points[j].y - points[i].y) / (points[j].x - points[i].x))
                dic[key] = (dic[key] + 1 if key in dic else 1)
            for key in dic:
                if dic[key] + dup > ans:
                    ans = dic[key] + dup
        return ans
