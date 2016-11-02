# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-30 00:30:20
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-30 00:36:19

# What can we do if we insert multiply times
# https://discuss.leetcode.com/topic/53458/facebook-interview-followup-how-to-improve-if-called-multiple-times/3


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ans = []
        i = 0
        while i < len(intervals):
            if intervals[i].end < newInterval.start:
                ans.append(intervals[i])
            else:
                break
            i += 1
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval.start = min(newInterval.start, intervals[i].start)
            newInterval.end = max(newInterval.end, intervals[i].end)
            i += 1
        ans.append(newInterval)
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
        return ans
