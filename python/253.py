# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-19 23:54:48
# @Last Modified time: 2016-11-19 23:55:23
# @FileName: 253.py


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        heap, num = [], 0
        intervals = [(i.start, i.end) for i in intervals]
        intervals.sort()
        for i in range(len(intervals)):
            if heap and heap[0] <= intervals[i][0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])
            num = max(num, len(heap))
        return num