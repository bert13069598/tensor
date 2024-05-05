import numpy as np
import torch

a = [1, 2, 3, 4, 5, 6]

a_np = np.array(a)
print(a_np)
a_np = a_np.reshape(2, 3)
print(a_np)

a_tensor = torch.tensor(a)
print(a_tensor)
a_tensor = a_tensor.view(2, 3)
print(a_tensor)

"""
[1 2 3 4 5 6]
[[1 2 3]
 [4 5 6]]
tensor([1, 2, 3, 4, 5, 6])
tensor([[1, 2, 3],
        [4, 5, 6]])
"""
