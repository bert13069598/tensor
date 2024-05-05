import numpy as np
import torch

a = [1, 2, 3]

a_np = np.array(a)
print(a_np)

a_tensor = torch.tensor(a)
print(a_tensor)

a_tensor = a_tensor.to('cuda:0')
print(a_tensor)

a_tensor = a_tensor.cpu()
print(a_tensor)

"""
[1 2 3]
tensor([1, 2, 3])
tensor([1, 2, 3], device='cuda:0')
tensor([1, 2, 3])
"""
