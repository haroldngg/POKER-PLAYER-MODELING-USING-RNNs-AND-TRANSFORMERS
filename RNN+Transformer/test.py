import torch

u = torch.tensor([1., 2., 3.])

print(torch.concat((u,u), dim=1))