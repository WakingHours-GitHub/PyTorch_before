import torch
from torch.utils.data import Dataset, DataLoader
import cv2 as cv
import os

# Dataset?? 直接打印官方说明
# utils就是torch的常用工具集
"""
常用的数据集分为两种, 
一种是分类的, 不同类别的数据集放在不同的文件夹中
或者是将数据集放在一个文件夹中, 将标签放在另一个文件夹, 中间通过某种形式进行对应.

首先我们看一下Dataset:
class Dataset(Generic[T_co]):
    An abstract class representing a :class:`Dataset`.
    All datasets that represent a map from keys to data samples should subclass
    it. All subclasses should overwrite :meth:`__getitem__`, supporting fetching a
    data sample for a given key. Subclasses could also optionally overwrite
    :meth:`__len__`, which is expected to return the size of the dataset by many
    :class:`~torch.utils.data.Sampler` implementations and the default options
    of :class:`~torch.utils.data.DataLoader`.
    
    一个抽象类, 所有的dataset都应该继承该类, 并且所有的子类都应该重写__getitem__这个方法, 支持你能够fetch(抓取)
    数据样本通过一个给定的key, 并且子类可以有选择的重写__len__, 该方法, 是返回该dataset的长度



"""


class MyDataset(Dataset):
    def __init__(self, train: bool = True, img_type: str = None):
        if img_type not in ["ants", "bees"]:
            print("error, parm: \"img_type\", should is ants or bees")
            raise RuntimeError  # 报错
        self.img_type = img_type
        __train_data_path = "./hymenoptera_data/train"
        __text_data_path = "./hymenoptera_data/val"
        # 是否训练.
        self.data_path = __train_data_path if train else __text_data_path
        self.all_file_root_path = os.path.join(self.data_path, self.img_type)  # 这样就得到了指定的所有文件的路径

        # 接下来我们获取图片:
        # 先获取, 目录文件夹下的所有文件, 然后和跟目录进行拼接
        self.all_file_path = [os.path.join(self.all_file_root_path, file_path) for file_path in
                              os.listdir(self.all_file_root_path)]

    def __getitem__(self, item):
        # 返回内容和标签
        return torch.tensor(cv.imread(self.all_file_path[item]), dtype=torch.float32), self.img_type  # 返回内容和标签

    def __len__(self):
        return len(self[::])


if __name__ == '__main__':
    ants_dataset = MyDataset(img_type="ants")
    bees_dataset = MyDataset(img_type="bees")
    train_dataset = ants_dataset + bees_dataset  # 可以将两个数据集加起来, 形成一个数据集合
