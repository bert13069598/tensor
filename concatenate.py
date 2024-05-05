import numpy as np
import torch

a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8, 9]]
c = [[7, 8]]

c_np = np.array(c).T

cat1 = np.concatenate((a, b), axis=0)
cat2 = np.concatenate((a, c_np), axis=1)
print(cat1)
print(cat2)

a_tensor = torch.tensor(a)
b_tensor = torch.tensor(b)
c_tensor = torch.tensor(c).T

cat3 = torch.cat((a_tensor, b_tensor), dim=0)
cat4 = torch.cat((a_tensor, c_tensor), dim=1)
print(cat3)
print(cat4)

"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[1 2 3 7]
 [4 5 6 8]]
tensor([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
tensor([[1, 2, 3, 7],
        [4, 5, 6, 8]])
"""
