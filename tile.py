import numpy as np
import torch

a = [1, 2, 3]

tile1 = np.tile(a, 3)
tile2 = np.tile(a, (3, 1))
tile3 = np.tile(a, (2, 3, 1))
print(tile1)
print(tile2)
print(tile3)

a_tensor = torch.tensor(a)
tile4 = torch.tile(a_tensor, (3,))
tile5 = torch.tile(a_tensor, (3, 1))
tile6 = torch.tile(a_tensor, (2, 3, 1))
print(tile4)
print(tile5)
print(tile6)

"""
[1 2 3 1 2 3 1 2 3]
[[1 2 3]
 [1 2 3]
 [1 2 3]]
[[[1 2 3]
  [1 2 3]
  [1 2 3]]

 [[1 2 3]
  [1 2 3]
  [1 2 3]]]
tensor([1, 2, 3, 1, 2, 3, 1, 2, 3])
tensor([[1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]])
tensor([[[1, 2, 3],
         [1, 2, 3],
         [1, 2, 3]],

        [[1, 2, 3],
         [1, 2, 3],
         [1, 2, 3]]])
 """

b = [[1], [2]]

b_tensor = torch.tensor(b)
tile7 = torch.tile(b_tensor, (2, 3, 4))
print(tile7)

"""
tensor([[[1, 1, 1, 1],
         [2, 2, 2, 2],
         [1, 1, 1, 1],
         [2, 2, 2, 2],
         [1, 1, 1, 1],
         [2, 2, 2, 2]],

        [[1, 1, 1, 1],
         [2, 2, 2, 2],
         [1, 1, 1, 1],
         [2, 2, 2, 2],
         [1, 1, 1, 1],
         [2, 2, 2, 2]]])
"""