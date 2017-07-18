# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 17:15:56
# @Last Modified time: 2016-11-17 17:15:57
# @FileName: 359.py


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.dic:
            self.dic[message] = timestamp
            return True
        elif timestamp - self.dic[message] >= 10:
            self.dic[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)