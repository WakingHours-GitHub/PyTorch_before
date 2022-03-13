import torch
from torch import  nn
from torch import optim

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# print(device) # cuda:0

# 准备数据:
x = torch.rand(size=(500, 1)).to(device)