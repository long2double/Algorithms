"""
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，因此只要知
道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一
支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。
弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

Example:
输入:
[[10,16], [2,8], [1,6], [7,12]]
输出:
2

解释:
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。
"""


class Solution:
    def findMinArrowShots(self, points) -> int:
        if points == []:
            return 0

        points.sort()
        shoot_num = 1
        start_left, end_right = points[0]
        # 维护一个小的区间，不断更新，直到下一个不在该区间，重新赋予新区间并加一个射手
        for left, right in points[1:]:
            if left <= end_right and right <= end_right:  # 已经排好序，左侧值只会越来越大, 只需考虑left<=end_right
                end_right = right
            elif left > end_right:
                end_right = right
                shoot_num += 1
        return shoot_num
