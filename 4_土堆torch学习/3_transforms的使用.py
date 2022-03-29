from torchvision import transforms
from torchvision.transforms import  *
import cv2 as cv



"""
transforms的结构与用法
    transforms.py -> 工具箱.
    
在python中的用法:
通过transforms.ToTensor去解决两个问题
    1. transforms应该如何使用
    2. Tensor数据类型, 是什么?
"""
# 使用cv2进行读取文件, ndarray数据类型
img = cv.imread("./hymenoptera_data/train/ants/0013035.jpg")

# 创建对象,
toTensor = transforms.ToTensor() # 返回一个实例
# 然后我们直接调用他的__call()__方法
img_tensor = toTensor(img)
print(img_tensor)




