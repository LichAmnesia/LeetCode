# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-19 12:39:52
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-19 12:39:54
# @Email: shen.huang@colorado.edu


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        def remove(ans, r, pa):
            if not r.left and not r.right:
                if pa.left == r:
                    pa.left = None
                else:
                    pa.right = None
                ans.append(r.val)
                return
            if r.left:
                remove(ans, r.left, r)
            if r.right:
                remove(ans, r.right, r)
        
        res = []
        pa = TreeNode(0)
        pa.left = root
        
        while pa.left:
            ans = []
            remove(ans, root, pa)
            if ans:
                res.append(ans[:])
            else:
                return res
        return res
        