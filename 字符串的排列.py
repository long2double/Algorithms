# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return [ss]
        res = set()
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i] + ss[i + 1:]):
                res.add(ss[i] + j)
        return sorted(res)