

import torch
from torch.utils.data import Dataset, DataLoader
import os,os.path






class IMBD_data_set(Dataset):
    def __init__(self):
        self.train_data_path = "./aclImdb_v1"


if __name__ == '__main__':

