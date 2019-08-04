# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        li = list(s)
        for index, key in enumerate(li):
            if key == ' ':
                li[index] = '%20'
        return ''.join(li)
