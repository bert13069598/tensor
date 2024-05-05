import numpy as np
import torch

a = [1, 2, 3]

a_np = np.array(a)

unsqueeze1 = a_np[np.newaxis, :]
print(unsqueeze1)
unsqueeze2 = np.expand_dims(a_np, axis=0)
print(unsqueeze2)
squeeze1 = unsqueeze1.squeeze()
print(squeeze1)

a_tensor = torch.tensor(a)

unsqueeze3 = a_tensor.unsqueeze(dim=0)
print(unsqueeze3)
squeeze2 = unsqueeze3.squeeze()
print(squeeze2)

"""
[[1 2 3]]
[[1 2 3]]
[1 2 3]
tensor([[1, 2, 3]])
tensor([1, 2, 3])
"""