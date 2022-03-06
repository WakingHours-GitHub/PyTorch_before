
"""

PyTorch 是基于Torch进行二次开发的。
是FaceBook阵营。

Google:
    TensorFlow1
    TensorFlow2
    +Keras
Facebook:
    Torch7
    Caffe
    PyTorch+Caffe2

目前十分主流的就是TensorFlow和PyTorch
这两个一个是静态图, 一个是动态图.
静态图:
    定义图, 然后运行(会话: 实际上是一个接口)之前的定义图

动态图:
    定义即运行. 简单, 灵活, 但是性能较低.

PyTorch在学术界更受欢迎
TensorFlow2在工业界更受欢迎

PyTorch生态:
    AllenNLP
    TorchVision
    PyTorch geometric
    Fast.ai
    ONNX协议, 部署在一个移动端设备.

PyTorch能够做什么:
    GPU加速: CUDA,来自nvidia的深度学习加速
    自动求导: 具备自动求导功能
    常用网络层: 有很多已经准备好的网络架构去供我们使用

安装开发环境:
    Python + Anaconda
    CUDA, 用于深度学习加速.
    PyCharm


梯度下降算法:
    梯度: gradient就是深度学习的精髓.
        整个deep learning就是靠梯度下降算法所支撑起来的.
    梯度下降, 就是将x* = x - y' 这样一个迭代的过程. 得到x*就是一个调整的速度(步长)
    当然有时候这个x*会比较大, 所以我们会将y'乘以一个learning rate, 用来控制这个速度

    那么梯度下降算法, 他会在这个理论值的最优解的附近进行波动
    learning rate设置的非常小的时候, 他迭代的更慢, 但是也更精准
    当learning rate设置的较大的时候, 迭代速度很快, 但是收敛于理论值就更加不精准
    初学者我们一般是将leaning rate设置为0.001.

    对于梯度下降算法, 拥有不同的求解器, 但本质上仍然是上面的公式, 只不过在一些约束条件和公式上做出了一些改进
    使得求解速度和求解精度都有不同程度的改进

    使用较多: SGD, RMS, ADAM

如何求解一个简单的二元一次方程组
    y = wx + b
    消元法, 得到一个精确解: close from solution


    但是我们对于深度学习任务: 我们不是直接求y的极大值或者极大值
    而是求解: loss = (WX + B - Y) ^ 2, 即: loss = (Y_pred - Y)^2 的最小值
    平方和, 是避免正负差异抵消, 并且方便求梯度.
    通过不断优化loss, 以达到 Y ~ Wx+B, 的效果
    当loss趋近于0时, 我们求解得到的也就是y~wx+b近似时的一个w,b的取值
    这样我们就给构建了一个优化目标, 即loss最小

    那么如果给定一堆点的情况下: 就是线性回归的情况:
    Linear Regression:
    loss就被定义为: loss = sum((Wx_i + b - y_i) ^ 2)
    通过不断优化这个loss, 我们估计得到一组w/b的值, 构建好这个回归方程
    然后再用来预测: x_pred -> y_pred
    一般来说: 回归问题的y是(-inf, +inf)的一个连续数值.

    Logistic Regression:
    就是回归的基础上, 加上了一个激活函数(压缩函数), 使y(-inf, +inf)坍塌到(0, 1)范围内, 此时就变成了概率问题,
    再logistic regression中, 这个激活函数称为: sigmoid函数

    Classification:
    分类问题. 所有类别的概率值加起来为1, 然后取最大的那个概率值, 作为类别.































"""