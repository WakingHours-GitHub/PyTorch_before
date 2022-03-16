import torch
from torch.utils.data import Dataset, DataLoader # 导入数据加载包

# 数据集来源: http://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
data_path = "./SMSSpamCollection"  # 保存的数据来源路径


# 完成数据集类:
class SMSS_dataset(Dataset):  # 继承Dataset父类
    def __init__(self):  # 构造函数, 直接执行
        self.lines = open(data_path, 'r', encoding="utf-8").readlines()  # 获取所有行

    def __getitem__(self, item): # 根据索引获取数据
        cur_line = self.lines[item].strip()
        # 切分成label和feature
        label = cur_line[0:4].strip()
        content = cur_line[4:].strip()
        return label, content




    def __len__(self):  # 返回数据的总数量
        return len(self.lines)



def test01():
    """
    使用继承dataset() 子类. 生成数据集类

    :return:
    """
    my_dataset = SMSS_dataset()  # 实例化对象
    print(my_dataset[2])  # 直接调用回调函数, 返回取回的值
    print(len(my_dataset)) #

    # 我们也可以进行遍历：
    for i in range(len(my_dataset)):
        print(my_dataset[i])

def test02():
    # 实例化数据集对象
    data_set = SMSS_dataset()



    dataloader = DataLoader(
        dataset=data_set, # 数据集对象
        batch_size=2, # batch, 分组大小
        shuffle=True, # 是否打乱
        num_workers=2 # 线程数
    )

    for dl in dataloader:
        print(dl)
        break

    # 我们经常会使用 enumerate
    for index, (label, content) in enumerate(dataloader):
        print(index, label, content)
        break

# 测试：
if __name__ == '__main__':
    test02()

