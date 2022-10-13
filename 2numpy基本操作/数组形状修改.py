import numpy as np


# 在前面的学习中，可以知道，ndarray是有shape的，中文译为形状，
# 在后续深度学习中，对于输入数据往往都有各自的要求，拿LSTM为例，要求输入的是一个三维张量，而数据往往会是一个二维矩阵，
# 那么为了能让神经网络模型能够使用我们处理好的数据，需要给数据增维度，而pandas的基本数据dataframe是不能增加维度的，
# 那么此时就可以将数据变成ndarray的格式，在ndarray中增加维度，再将处理好的ndarray数据，转换成dataframe输入神经网络模型。
# 因此，numpy的ndaray一个重要功能就是改变数组的维度(升维和降维)，方便后续操作，还有一个通用功能，数组的转置，即沿着对角线一个翻转，

a=np.random.normal(1,5,[4,5])  # 构造一个5行4列的随机数组
print(a)
# 数组升降维
# 1.ndarray.reshape(shape)
a1=a.reshape([2,2,5])  # 将二维矩阵升维到了三维张量，一个计算方法，数据总数不变原则，如4行5列的矩阵，可以变成2个2行5列的矩阵组成的张量，完成升维
print(a1,a1.shape)

a2=a.reshape([20])  # 二维矩阵变成一个长度20的向量，降维
print(a2,a2.shape)

print(a.reshape([5,4]),'reshape')

# 对原数组上进行，shape的改变，和原shape不一样，
# 2.ndarray.resize()
# 不好用
# 建议别用

# 对数组转置
# 3.ndarray.T
c=np.random.normal(1,2,[2,3])
print('c{}'.format(c))
print('c转置{},shape{}'.format(c.T,c.T.shape))

# 数组多维变一维，如二维，三维
# 4.ndarray.ravel
d=np.random.normal(1,3,[2,2,3])
print('d{}'.format(d))
d1=d.ravel()  # 三维张量变成一维向量
print('d1{}'.format(d1))

# 数组多维变成一维，可以是二维，三维
# 5.ndarray.flatten

print('d{}'.format(d))

e1=d.flatten()
print('e1{}'.format(e1))







































