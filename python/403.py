# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-18 16:46:56
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-18 16:46:56
# @Email: shen.huang@colorado.edu


# (x, y) x is the position. y represent the last unit
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        q = collections.deque()
        vis = collections.defaultdict(lambda : collections.defaultdict(bool))
        stones_set = set(stones)
        q.append((0, 0))
        vis[0][0] = True
        while q:
            x, y = q.popleft()
            if x == stones[-1]: return True
            for z in (y - 1, y, y + 1):
                if z > 0 and not vis[x + z][z] and x + z in stones_set:
                    q.append((x + z, z))
                    vis[x + z][z] = True
        return False