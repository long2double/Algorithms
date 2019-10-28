class Solution:
    def IOU(self, boxA: list, boxB: list):
        """"
            left top, right bottom
            boxA: x1, y1, x2, y2
            boxB: x3, y3, x4, y4
        """
        A_width = boxA[2] - boxA[0]
        A_high = boxA[3] - boxA[1]
        B_width = boxB[2] - boxB[0]
        B_high = boxB[3] - boxB[1]

        width = min(boxA[0], boxA[2], boxB[0], boxB[2]) + A_width + B_width - max(boxA[0], boxA[2], boxB[0], boxB[2])
        high = min(boxA[1], boxA[3], boxB[1], boxB[3]) + A_high + B_high - max(boxA[1], boxA[3], boxB[1], boxB[3])

        if width <= 0 or high <= 0:
            return 0

        return width * high / (A_width * A_high + B_width * B_high - width * high)




