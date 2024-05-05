import numpy as np
import torch

a = [
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12]],
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12]],
]

a_np = np.array(a)
print(a_np.shape)

transpose1 = a_np.transpose((2, 0, 1))
print(transpose1.shape)

a_tensor = torch.tensor(a)
print(a_tensor.shape)
transpose2 = a_tensor.transpose(0, 2)
print(transpose2.shape)
transpose3 = a_tensor.permute(2, 0, 1)
print(transpose3.shape)

"""
(2, 4, 3)
(3, 2, 4)
torch.Size([2, 4, 3])
torch.Size([3, 4, 2])
torch.Size([3, 2, 4])
"""