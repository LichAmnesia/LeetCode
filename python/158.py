# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-13 11:13:34
# @Last Modified time: 2016-11-13 11:13:45
# @FileName: 158.py



# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.q = collections.deque()
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        #  队列不为空时，先读取队列中的暂存字符
        while i < n and self.q:
            buf[i] = self.q.popleft()
            i += 1
        
        while i < n:
            tmp = [""] * 4
            len_ = read4(tmp)
            # 如果读到字符多于我们需要的字符，需要暂存这些多余字符
            if len_ > n - i:
                buf[i: n] = tmp[:n - i]
                for j in range(n - i, len_):
                    self.q.append(tmp[j])
            else:
                # 如果读到的字符少于我们需要的字符，直接拷贝
                buf[i:i + len_] = tmp[:len_]
            # 同样的，如果读不满4个，说明数据已经读完，返回总所需长度和目前已经读到的长度的较小的
            if len_ < 4: return min(i + len_, n)
            i += 4
        
        return n