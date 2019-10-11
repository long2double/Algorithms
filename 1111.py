import numpy as np
import torch


a = np.array([[[1,2,3],[4,5,6]]])

un = torch.tensor(a)
print(un)
# print(un.size())
per = un.permute(2,0,1)
print(per)
print(per.shape)
# print(per.size())