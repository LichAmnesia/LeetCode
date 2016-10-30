# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-30 01:10:30
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-30 01:10:56

# Can use another method to hadle this problem. pre-order 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque()
        q.append(root)
        res = []
        if not root:
            return ''
        while q:
            node = q.popleft()
            if not node:
                res.append('#')
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        while res[-1] == '#':
            res.pop()
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # def dfs():
        #     val = next(vals)
        #     print val
        #     if val == '#':
        #         return None
        #     node = TreeNode(int(val))
        #     node.left = dfs()
        #     node.right = dfs()
        #     return node

        # vals = iter(data.split())
        # print vals
        # return dfs()
        if not data:
            return None
        vals = data.split()
        vals = vals[::-1]
        q = collections.deque()
        root = TreeNode(int(vals.pop()))
        q.append(root)

        while q and vals:
            node = q.popleft()
            tmp = vals.pop()
            node.left = TreeNode(int(tmp)) if tmp != '#' else None
            if node.left:
                q.append(node.left)

            if vals:
                tmp = vals.pop()
                node.right = TreeNode(int(tmp)) if tmp != '#' else None
                if node.right:
                    q.append(node.right)

        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
