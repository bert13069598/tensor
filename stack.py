import numpy as np
import torch

a = [1, 2, 3]
b = [4, 5, 6]

stack1 = np.stack((a, b))
stack2 = np.stack((a, b),axis=1)
print(stack1)
print(stack2)


a_tensor = torch.tensor(a)
b_tensor = torch.tensor(b)
stack3 = torch.stack((a_tensor, b_tensor))
stack4 = torch.stack((a_tensor, b_tensor), dim=1)
print(stack3)
print(stack4)

"""
[[1 2 3]
 [4 5 6]]
[[1 4]
 [2 5]
 [3 6]]
tensor([[1, 2, 3],
        [4, 5, 6]])
tensor([[1, 4],
        [2, 5],
        [3, 6]])
"""
