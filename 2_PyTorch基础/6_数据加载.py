import torch
from torch.utils.data import Dataset  # 导入数据加载包

# 数据集来源: http://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
data_path = "./SMSSpamCollection"  # 保存的数据来源路径


# 完成数据集类:
class SMSS_dataset(Dataset):  # 继承Dataset父类
    def __init__(self):  # 构造函数, 直接执行
        self.liens = open(data_path, 'r', encoding="utf-8").readlines()  # 获取所有行

    def __getitem__(self, index):  # 获取对应索引的数据
        return self.lines[index].strip()

    def __len__(self):  # 返回数据的总数量
        return len(self.liens)


# 测试：
if __name__ == '__main__':
    my_dataset = SMSS_dataset()  # 实例化对象
    print(my_dataset.__getitem__(0))  # 直接调用回调函数
    print(len(my_dataset))
