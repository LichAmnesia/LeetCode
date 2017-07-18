# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-01 22:09:16
# @Last Modified time: 2016-11-01 22:13:59
# @FileName: 56.py

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 1: return []
        
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        ans = [intervals[0]]
        
        for idx, node in enumerate(intervals):
            if ans[-1].end >= node.start:
                ans[-1].end = max(node.end, ans[-1].end)
            else:
                ans.append(node)
        return ans