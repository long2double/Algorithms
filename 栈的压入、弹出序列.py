# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        # stack = []
        # for i in pushV:
            # stack.append(i)
            # while len(stack) != 0:
                # if stack[-1] == popV[0]:
                    # stack.pop()
                    # popV.pop(0)
                # else:
                    # break
        # return len(popV) == 0
        stack = []
        while popV:
            if pushV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            elif stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True