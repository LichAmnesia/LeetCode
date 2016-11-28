# -*- coding: utf-8 -*-
# @Author: Lich_
# @Date:   2016-11-27 15:32:32
# @Last Modified by:   Lich_
# @Last Modified time: 2016-11-27 15:39:29

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        max_x, min_x, mid_x = -sys.maxint, sys.maxint, 0
        dic = collections.defaultdict(set)
        for i in range(len(points)):
        	max_x = max(points[i][0], max_x)
        	min_x = min(points[i][0], min_x)
        	dic[points[i][0]].add(points[i][1])
        mid_x = (max_x + min_x)
        for i in range(len(points)):
        	tmp = mid_x - points[i][0] 
        	if tmp not in dic or points[i][1] not in dic[tmp]:
        		return False
        return True