import numpy as np
import torch

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a_np = np.array(a)
split1 = np.split(a_np, 3)
print(split1)

a_tensor = torch.tensor(a)
split2 = torch.split(a_tensor, 3)
print(split2)
