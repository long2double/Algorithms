import numpy as np


class Solution:
    def conv(self, input, kernel, flag='same'):
        k_h, k_w = kernel.shape
        if flag == 'valid':
            i_h, i_w = input.shape
            o_h, o_w = i_h - k_h + 1, i_w - k_w + 1
        else:
            o_h, o_w = input.shape
            p_h = k_h // 2
            p_w = k_w // 2
            # （（上，下），（左，右））
            input = np.pad(input, ((p_h, p_h), (p_w, p_w)), 'constant')

        out_tensor = np.zeros((o_h, o_w))
        for i in range(o_h):
            for j in range(o_w):
                out_tensor[i][j] = self.computer_conv(input, kernel, i, j)
        return out_tensor

    def computer_conv(self, input, kernel, i, j):
        res = 0
        k_h, k_w = kernel.shape
        for r in range(k_h):
            for c in range(k_w):
                res += input[i + r][j + c] * kernel[r][c]
        return res


if __name__ == '__main__':
    S = Solution()
    a = np.array([[1, 2, 3, 1],
                  [0, 2, 1, 0],
                  [1, 0, 1, 0]])

    b = np.array([[1, 0, 1],
                  [1, 1, 1],
                  [0, 1, 0]])
    print(S.conv(a, b))
